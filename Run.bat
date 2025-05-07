@echo off
call .venv\Scripts\activate
pytest Tests/test_orangehrm.py --html=report.html