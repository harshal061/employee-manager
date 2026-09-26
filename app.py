# app.py

from employees import get_employees

employees = get_employees()

for employee in employees:
    print(employee)