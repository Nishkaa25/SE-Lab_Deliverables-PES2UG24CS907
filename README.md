# Software Engineering Lab Deliverables

**Student:** Nishkaa V  
**SRN:** PES2UG24CS907  
**Class:** 5-B  
**University:** PES University

## Lab Deliverables

| Lab | Topic | Deliverables |
|-----|-------|--------------|
| 1 | Software Requirements Engineering | Requirements table, UML use-case diagram and use-case specification |
| 2 | Agile Project Management with Jira | Epics, user stories, sprint boards, burndown charts and reflections |
| 3 | Software Architecture | Microservices architecture justification and UML component diagram |
| 4 | Vibe Coding - Rock Paper Scissors | Pygame source code, before/after videos and chat history |
| 5 | Static Code Analysis | Corrected Python code, issue documentation, reflection and Pylint/Bandit/Flake8 reports |

## Lab 2 - Agile Project Management with Jira

**Project:** Community Lost & Found Matching Network

**Jira Board:**
https://nishkaav.atlassian.net/jira/software/c/projects/CLFMN/boards/35/backlog

Deliverables:
- Epics and User Stories
- Product Backlog
- Sprint Planning and Story Points
- Sprint Board
- Burndown Charts
- Reflection Questions

Screenshots and documentation are available in `Lab_02_Jira_Agile/`.

## Lab 4 Repository
https://github.com/Nishkaa25/59_rock_paper_scissor

## Lab 5 Repository
https://github.com/Nishkaa25/L5_60_hostel-room-allocation

Lab 5 Static Analysis Results :
- Pylint: 10.00/10
- Bandit: 0 issues
- Flake8: 0 issues

## Lab 6 – Branch Coverage Testing: Phone Repair Quote

This lab focuses on branch coverage testing using the Phone Repair Quote application.

The implementation, test cases, supporting documentation and other lab deliverables are included in `Lab_06_Branch_Coverage/`.

**Source Repository:** [L6_L7_59_phone_repair_quote](https://github.com/Nishkaa25/L6_L7_59_phone_repair_quote)

## Lab 7 – Fuzz Testing for Input Validation Bugs

This lab explores property-based fuzz testing using the Hypothesis library to identify input validation bugs in a Python-based Phone Repair Quote parser.

The three functions tested are:
- `mask_imei()` – IMEI masking
- `parse_parts_order()` – Parts and quantity parsing
- `parse_model()` – Phone brand and model parsing

Hypothesis was used to generate unexpected inputs and expose edge cases. The original implementation was then hardened with input validation and defensive programming, followed by successful test execution.

The folder contains the original and completed lab materials, application code, tests and supporting report.

**Source Repository:** [L6_L7_59_phone_repair_quote](https://github.com/Nishkaa25/L6_L7_59_phone_repair_quote)

**Test Result:** 3 Hypothesis tests passed.
