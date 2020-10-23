import re
import json
from Project1.database import *

class Employee:
    def __init__(self, first_name: str, last_name: str, role: str, annual_salary: float, feedback: int,
                 years_employed: int, email: str):
        self.first_name = first_name
        self.last_name = last_name
        self.role = role
        self.annual_salary = annual_salary
        self.feedback = feedback
        self.years_employed = years_employed
        self.email = email

    def __str__(self):
        return f"{self.first_name}, {self.last_name}, {self.role}, {self.annual_salary}, {self.feedback}, {self.years_employed}, {self.email}"

    @classmethod
    def create_from_string(cls, employee_string: str):
        first_name, last_name, role, annual_salary, feedback, years_employed, email = employee_string.split()
        annual_salary, feedback, years_employed = float(annual_salary), int(feedback), int(years_employed)
        if cls.validate_email(email):
            return cls(first_name, last_name, role, annual_salary, feedback, years_employed, email)

    @staticmethod
    def validate_email(email):
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        if re.search(regex, email):
            return True
        return False

employee1 = Employee.create_from_string("jonas biliunas CFO 2000.0 10 5 j.biliunas@gnail.com")
print(employee1)

#Employee_works_three_years = lambda x: x > 3
#if Employee_works_three_years(employee1.years_employed):
 #  database.create_employee(employee1.first_name, employee1.last_name, employee1.role, employee1.annual_salary,employee1.feedback, employee1.years_employed, employee1.email)

with open('company_employees.json') as in_file:
    empl = json.load(in_file)

with open('feedback_for_employees.json') as in_file:
    feed = json.load(in_file)

print(empl["Employees"])
print(empl)

for employee in [object1, object2]
    create_employee(employee.first_name)



