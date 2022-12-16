import json
import random

class Employee:
    def __init__(self, data):
        d = json.load(data)
        self.year = d['year']
        self.month = d['month']
        self.salary = d['salary']

class HourWage:
    def __init__(self):
        self.year_month_hours = {}

    def calculate_hour_wage(self, employee):
        year = self.year_month_hours.get(employee.year, {})
        work_hours = year.get(employee.month, random.randint(20, 23))
        hour_income = round(employee.salary / work_hours, 2)
        return hour_income

    def update_json(self, employee):
        hour_income = self.calculate_hour_wage(employee)
        out = {"year": employee.year, "month": employee.month, "salary": employee.salary, "hour_income": hour_income}
        return json.dumps(out, indent=4)


data = open("../input.json")
employee1 = Employee(data)
wage_cnt = HourWage()
ans = wage_cnt.update_json(employee1)
f = open("../output.json", "w")
f.write(ans)
f.close()



