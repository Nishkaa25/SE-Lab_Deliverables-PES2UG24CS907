# Lab 5: Static Code Analysis - Reflection

**Note:** The supplied 4-page handout mentions reflection questions but does not contain their text. These are four SUGGESTED questions and draft answers, not the missing instructor-issued questions. Replace them if your faculty provides the original set.

## 1. What did you learn from running static analysis tools?

Static analysis examines source code without executing it. Pylint highlighted maintainability and coding-style problems, Bandit helped identify potentially insecure patterns, and Flake8 checked syntax, formatting, and PEP 8 style. Reading the reports made it easier to prioritize fixes rather than changing code randomly.

## 2. How are Pylint, Bandit, and Flake8 different?

Pylint focuses on quality issues, naming conventions, and possible errors. Bandit looks for known security-related coding patterns such as unsafe YAML loading or debug settings. Flake8 focuses on style and common source-level errors. They overlap sometimes, but they check different aspects of the code.

## 3. Which issues had the greatest impact, and why?

I prioritized unsafe YAML loading, credentials embedded in source code, and running Flask with debugging enabled because of security risk. I also corrected allocation capacity limits and room-vacating behavior because incorrect occupancy can break the hostel's core functionality.

## 4. Can static analysis guarantee that a program is correct?

No. Static tools can miss logical mistakes such as incorrect vacant-bed counts or failure to remove occupants from a room. After fixing warnings, I ran the program and validated room occupancy, gender restrictions, duplicate registration, student removal, fee calculation, and seniority order to verify behavior.
