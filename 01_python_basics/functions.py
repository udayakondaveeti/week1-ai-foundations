# Functions with parameters and return values

def add_numbers(a, b):
    return a + b


def greet(name, title="Engineer"):
    return f"Hello {title} {name}"


print(add_numbers(10, 20))
print(greet("Aisha"))
print(greet("Ben", "Data Scientist"))
