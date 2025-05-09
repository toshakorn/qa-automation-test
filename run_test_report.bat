@echo off
pytest test-login.py --html=report.html --self-contained-html --metadata project HerokuApp --metadata tester jamei
start report.html
pause
REM This script runs the test-login.py file using pytest and generates an HTML report.
REM The report is saved as report.html and opened in the default web browser.