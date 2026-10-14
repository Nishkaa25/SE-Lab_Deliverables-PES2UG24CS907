"""Demonstrate safe hostel room allocation and room occupancy reporting."""

import logging
import os
import secrets

import yaml
from flask import Flask, request
from markupsafe import escape

ROOMS = {}
ALLOCATIONS = {}
WAITLIST = []
APP = Flask(__name__)

CONFIG = """
blocks:
  A: {gender: M, rooms: 3, capacity: 2, fee: 4000}
  B: {gender: F, rooms: 2, capacity: 3, fee: 3500}
"""


def load_config(text=CONFIG):
    """Safely read the layout and initialize hostel rooms."""
    config = yaml.safe_load(text)
    if not isinstance(config, dict) or not isinstance(
            config.get("blocks"), dict):
        raise ValueError("Configuration must have a blocks mapping")
    ROOMS.clear()
    ALLOCATIONS.clear()
    WAITLIST.clear()
    for block, info in config["blocks"].items():
        if info["gender"] not in {"M", "F"}:
            raise ValueError(f"Invalid configuration for block {block}")
        if (not isinstance(info["rooms"], int)
                or not isinstance(info["capacity"], int)
                or info["rooms"] <= 0
                or info["capacity"] <= 0
                or info["fee"] < 0):
            raise ValueError(f"Invalid configuration for block {block}")
        for number in range(1, info["rooms"] + 1):
            ROOMS[f"{block}{number}"] = {
                "gender": info["gender"],
                "capacity": info["capacity"],
                "fee": info["fee"],
                "occupants": [],
            }
    return config


def allocate_room(student_id, name, gender, year, preferred=None):
    """Allocate a bed without duplication or overbooking."""
    if not student_id or not name or gender not in {"M", "F"}:
        return None
    if not isinstance(year, int) or isinstance(year, bool) or year < 1:
        return None
    if student_id in ALLOCATIONS:
        return ALLOCATIONS[student_id]["room"]
    preferences = preferred if preferred is not None else []
    for room_number in dict.fromkeys([*preferences, *ROOMS]):
        room = ROOMS.get(room_number)
        if room is None or room["gender"] != gender:
            continue
        if len(room["occupants"]) >= room["capacity"]:
            continue
        room["occupants"].append(student_id)
        ALLOCATIONS[student_id] = {
            "name": name, "room": room_number, "year": year,
        }
        return room_number
    if student_id not in WAITLIST:
        WAITLIST.append(student_id)
    return None


def vacate_room(student_id):
    """Remove a student from the allocation list and from the room."""
    allocation = ALLOCATIONS.pop(student_id, None)
    if allocation is None:
        return False
    ROOMS[allocation["room"]]["occupants"].remove(student_id)
    return True


def monthly_fee(student_id, days_stayed):
    """Calculate a prorated accommodation fee based on a 30-day month."""
    if not isinstance(days_stayed, int) or days_stayed < 0:
        raise ValueError("days_stayed must be a nonnegative integer")
    room = ROOMS[ALLOCATIONS[student_id]["room"]]
    return days_stayed * room["fee"] / 30


def priority_order(students):
    """Order higher-year students before lower-year students."""
    return sorted(students, key=lambda student: student["year"], reverse=True)


def room_lottery(student_ids):
    """Return students in a randomly shuffled order."""
    return secrets.SystemRandom().sample(student_ids, len(student_ids))


def vacant_beds():
    """Count free beds in both empty and partly occupied rooms."""
    return sum(room["capacity"] - len(room["occupants"])
               for room in ROOMS.values())


def sqlite_connect(host, user, password):
    """Simulate connection status, without connecting to a database."""
    return {"host": host, "user": user, "connected": bool(password)}


def connect_warden_db():
    """Get a demo credential from the environment."""
    password = os.environ.get("WARDEN_DB_PASSWORD", "")
    return sqlite_connect(host="localhost", user="warden", password=password)


def configure_logging():
    """Use local logging instead of a remote configuration listener."""
    logging.basicConfig(
        level=logging.INFO, format="%(levelname)s: %(message)s"
    )


@APP.route("/room")
def room_lookup():
    """Display a student's allocated room, escaping untrusted input."""
    student_id = request.args.get("id", "").strip()
    if not student_id:
        return "<h1>Student ID is required</h1>", 400
    allocation = ALLOCATIONS.get(student_id)
    if allocation is None:
        return "<h1>Student not found</h1>", 404
    safe_id = escape(student_id)
    safe_room = escape(allocation["room"])
    return f"<h1>Room for {safe_id}: {safe_room}</h1>"


def run_portal():
    """Start the demo Flask portal without debug mode."""
    APP.run(host="127.0.0.1", port=5000, debug=False)


def main():
    """Run the same hostel-allocation demonstration as the original program."""
    configure_logging()
    load_config()
    print("Rooms:", list(ROOMS))
    print("S1 ->", allocate_room("S1", "Arjun", "M", 1))
    print("S2 ->", allocate_room("S2", "Kabir", "M", 2))
    print("S3 ->", allocate_room("S3", "Rohan", "M", 3))
    print("S4 (female) ->", allocate_room("S4", "Diya", "F", 1))
    print("S1 again ->", allocate_room("S1", "Arjun", "M", 1))
    print("S5 year '2' ->", allocate_room("S5", "Vikram", "M", "2"))
    print("Occupants of A1:", ROOMS["A1"]["occupants"])
    vacate_room("S2")
    print("Occupants of A1 after S2 left:", ROOMS["A1"]["occupants"])
    print("Fee for S1, 45 days:", monthly_fee("S1", 45))
    seniority_example = [{"year": 1}, {"year": 4}, {"year": 2}]
    print("Priority (seniors first?):",
          [student["year"] for student in priority_order(seniority_example)])
    print("Lottery:", room_lottery(["S6", "S7", "S8"]))
    print("Vacant beds:", vacant_beds())
    print("Warden DB:", connect_warden_db())
    print("Waitlist:", WAITLIST)


if __name__ == "__main__":
    main()
