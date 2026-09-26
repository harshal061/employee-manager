# app.py

from employees import get_employees

employees = get_employees()

for employee in employees:
    print(employee)
    if employee.startswith('A'):
        print('its amit')
    elif employee.startswith('H'):
        print('its harshal')
    elif employee.startswith('m'):
        print('its masterperson')
    else:
        continue