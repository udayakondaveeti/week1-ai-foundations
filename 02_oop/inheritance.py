# Inheritance example
class Person:
    def __init__(self, name):
        self.name = name

    def intro(self):
        return f"My name is {self.name}"


class Student(Person):
    def __init__(self, name, course):
        super().__init__(name)
        self.course = course

    def intro(self):
        return f"{super().intro()} and I study {self.course}"


student = Student("Mina", "Artificial Intelligence")
print(student.intro())
