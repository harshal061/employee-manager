# app.py

from employees import get_employees

employees = get_employees()

for employee in employees:
    print(employee)


def login(username, password):
    if username == "admin" and password == "1234":
        return "Login successful"
    return "Invalid credentials"