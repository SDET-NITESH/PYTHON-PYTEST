@echo off
cmd /k "cd /d C:\regress_venv\Scripts & activate  & cd /d  C:\Users\nitesh.agarwal\PycharmProjects\centime_pytest_framework\test_script & pytest get_time_series.py   --alluredir C:\Users\nitesh.agarwal\PycharmProjects\centime_pytest_framework\test_result & cd /d C:\Users\nitesh.agarwal\PycharmProjects\centime_pytest_framework\test_result & allure generate --clean C:\REPORTS
pause