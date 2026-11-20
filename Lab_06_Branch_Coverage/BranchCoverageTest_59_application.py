
import pytest
from phone_repair_quote import repair_quote, repair_days, trade_in_value


# ================= REPAIR QUOTE TESTS =================

# Example test cases
def test_budget_screen():
    assert repair_quote("screen", "budget", False, False) == 4600


def test_in_stock_quick():
    assert repair_days("battery", True, 2) == 1


# Valid parts and brand tiers
def test_budget_battery():
    assert repair_quote("battery", "budget", False, False) == 1800


def test_flagship_battery():
    assert repair_quote("battery", "flagship", False, False) == 3300


def test_flagship_screen():
    assert repair_quote("screen", "flagship", False, False) == 8600


def test_budget_camera():
    assert repair_quote("camera", "budget", False, False) == 2800


def test_flagship_camera():
    assert repair_quote("camera", "flagship", False, False) == 5300


def test_charging_port():
    assert repair_quote("charging_port", "budget", False, False) == 1100


# Invalid inputs
def test_unknown_part():
    with pytest.raises(ValueError):
        repair_quote("speaker", "budget", False, False)


def test_unknown_brand():
    with pytest.raises(ValueError):
        repair_quote("battery", "premium", False, False)


# Warranty conditions
def test_warranty_non_screen():
    assert repair_quote("battery", "budget", True, False) == 300


def test_warranty_screen():
    assert repair_quote("screen", "budget", True, False) == 4600


def test_warranty_flagship_camera():
    assert repair_quote("camera", "flagship", True, False) == 300


# Express repair conditions
def test_express_repair():
    assert repair_quote("battery", "budget", False, True) == 2300


def test_warranty_express_repair():
    assert repair_quote("battery", "budget", True, True) == 800


# ================= REPAIR DAYS TESTS =================

# Technician availability
def test_no_technicians():
    assert repair_days("battery", True, 0) == 3


def test_technicians_available():
    assert repair_days("battery", True, 2) == 1


# Parts availability
def test_screen_out_of_stock():
    assert repair_days("screen", False, 1) == 6


def test_camera_out_of_stock():
    assert repair_days("camera", False, 1) == 6


def test_battery_out_of_stock():
    assert repair_days("battery", False, 1) == 3


def test_charging_port_out_of_stock():
    assert repair_days("charging_port", False, 0) == 5


def test_screen_in_stock_no_technicians():
    assert repair_days("screen", True, 0) == 3


# ================= TRADE IN VALUE TESTS =================

# Age-based trade-in values
def test_trade_in_under_12_months():
    assert trade_in_value(10000, 6, False) == 6000


def test_trade_in_exactly_12_months():
    assert trade_in_value(10000, 12, False) == 6000


def test_trade_in_24_months():
    assert trade_in_value(10000, 24, False) == 4000


def test_trade_in_36_months():
    assert trade_in_value(10000, 36, False) == 2000


def test_trade_in_exactly_48_months():
    assert trade_in_value(10000, 48, False) == 2000


def test_trade_in_above_48_months():
    assert trade_in_value(10000, 49, False) == 0


# Cracked screen condition
def test_trade_in_cracked_screen():
    assert trade_in_value(10000, 12, True) == 3000


def test_trade_in_cracked_screen_24_months():
    assert trade_in_value(10000, 24, True) == 2000


def test_trade_in_uncracked_screen():
    assert trade_in_value(10000, 12, False) == 6000


# Invalid trade-in inputs
def test_zero_original_price():
    with pytest.raises(ValueError):
        trade_in_value(0, 12, False)


def test_negative_original_price():
    with pytest.raises(ValueError):
        trade_in_value(-1000, 12, False)


def test_negative_age():
    with pytest.raises(ValueError):
        trade_in_value(10000, -1, False)
