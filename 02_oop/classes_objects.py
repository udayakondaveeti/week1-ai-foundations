# Classes and objects
class Employee:
    def __init__(self, employee_id, name, department):
        self.employee_id = employee_id
        self.name = name
        self.department = department

    def describe(self):
        return f"{self.name} works in {self.department}"


emp1 = Employee(101, "Aisha", "Engineering")
emp2 = Employee(102, "Ben", "Data")
print(emp1.describe())
print(emp2.describe())
