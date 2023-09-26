class Employee:
    def __init__(self, name, salary, emp_date):
        self.name = name
        self.salary = salary
        self.emp_date = emp_date

    @staticmethod
    def years_employed():
        years = 2023 - int(p1.emp_date[:4])
        return years


p1 = Employee('Johan', 40235, '2020-09-22')
print(p1.years_employed())




