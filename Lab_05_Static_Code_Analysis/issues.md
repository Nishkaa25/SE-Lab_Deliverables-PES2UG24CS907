# Lab 5: Identified issues and fixes

Line numbers refer to the ORIGINAL `hostel_allocation.py` in the assigned GitHub repository. They change after fixes.

| Issue | Type | Line(s) | Description | Fix Approach |
|---|---|---|---|---|
| Unsafe YAML deserialization | Security | 18 | `yaml.load(..., Loader=yaml.Loader)` allows unsafe deserialization of YAML content. | Use `yaml.safe_load` and validate the parsed configuration. |
| Mutable default argument | Bug / Pylint | 25 | `preferred=[]` is shared between function calls. | Default to `None`, then create a new list when required. |
| Unsafe preferred room lookup | Bug | 28-29 | A nonexistent preferred room causes `KeyError`. | Use `rooms.get` and skip unknown rooms. |
| Capacity overflow | Bug | 30 | Checking `>` allows occupancy at full capacity to increase further. | Check `>=` before assigning. |
| Gender mismatch | Bug | 28-34 | Student gender is not checked against room gender. | Only allow gender-compatible rooms. |
| Duplicate registration | Bug | 32-34 | A student ID can be added multiple times. | Return the existing allocation instead of appending again. |
| Incomplete vacancy handling | Bug | 36-40 | `vacateRoom` deletes the map entry but leaves the occupant in the room. | Remove the student from both structures. |
| Wrong priority order | Bug | 47-48 | Default `sorted` puts first-year students before senior students. | Use `reverse=True`. |
| Wrong vacant-bed count | Bug | 52-57 | Only fully empty rooms contribute to vacant bed count. | Sum `capacity - current occupants` for each room. |
| Credential hardcoded in source | Security | 59-60 | The source includes a password string. | Read an optional demo credential from `WARDEN_DB_PASSWORD` environment variable. |
| Remote logging configuration | Security | 65-66 | A remote configuration listener can be unsafe if exposed or started. | Use local `logging.basicConfig` instead. |
| Unescaped HTML | Security | 68-70 | Student-controlled query parameters are concatenated into HTML. | Validate the identifier and HTML-escape rendered values. |
| Flask debugging | Security | 72-73 | The portal starts Flask with `debug=True`. | Run with `debug=False` bound to localhost. |
| Top-level main call | Style / Testability | 92 | Importing the script immediately executes `main()`. | Add an `if __name__ == "__main__":` guard. |
| Prorating fee | Behavior | 42-45 | Integer division silently discards a partial month. | Adopt and document a 30-day prorating rule. Confirm with instructor if whole-month billing is desired. |

**Important:** This table includes code-inspection bugs as well as issues static analyzers can detect. Match tool-specific warnings and exact severities to your own `*_before.txt` files; don't claim every issue was reported by Bandit, Flake8, or Pylint.

## Final Pylint cleanup (after initial remediation)

The first corrected version scored **9.80/10** with two remaining
`R0916` (`too-many-boolean-expressions`) warnings. Both have now been
addressed without suppressing warnings:

- Former corrected-code line 33: split room gender validation from the remaining configuration checks.
- Former corrected-code line 52: split student identity/gender checks from study-year validation.

Run Pylint again on the latest file to record the verified final score.
