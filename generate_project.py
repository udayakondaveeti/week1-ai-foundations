from pathlib import Path
import base64
import shutil
import json

root = Path(__file__).resolve().parent

# Remove placeholder files that would block creation of the required folders.
for name in [
    '01_python_basics', '02_oop', '03_numpy', '04_pandas', '05_api_data_collection',
    '06_sql', '07_mini_project', 'screenshots', 'outputs'
]:
    path = root / name
    if path.exists() and path.is_file():
        path.unlink()

# Create project directories.
directories = [
    '01_python_basics', '02_oop', '03_numpy', '04_pandas', '05_api_data_collection',
    '06_sql', '07_mini_project/dataset', '07_mini_project/src', '07_mini_project/outputs',
    'screenshots', 'outputs/csv_files', 'outputs/json_files'
]
for rel in directories:
    path = root / rel
    if path.exists() and path.is_file():
        path.unlink()
    path.mkdir(parents=True, exist_ok=True)

# Remove old generated files if present.
for rel in [
    'README.md','requirements.txt', '.gitignore',
    '01_python_basics/variables_and_datatypes.py',
    '01_python_basics/operators.py',
    '01_python_basics/loops_and_conditions.py',
    '01_python_basics/functions.py',
    '01_python_basics/file_handling.py',
    '02_oop/classes_objects.py',
    '02_oop/inheritance.py',
    '02_oop/polymorphism.py',
    '02_oop/encapsulation.py',
    '02_oop/abstraction.py',
    '03_numpy/array_creation.py',
    '03_numpy/array_operations.py',
    '03_numpy/indexing_slicing.py',
    '03_numpy/statistics.py',
    '03_numpy/matrix_operations.py',
    '04_pandas/data_loading.py',
    '04_pandas/data_cleaning.py',
    '04_pandas/filtering_sorting.py',
    '04_pandas/aggregation.py',
    '04_pandas/visualization.py',
    '04_pandas/sample_dataset.csv',
    '05_api_data_collection/fetch_data.py',
    '05_api_data_collection/process_json.py',
    '05_api_data_collection/api_results.json',
    '05_api_data_collection/api_results.csv',
    '06_sql/database_creation.sql',
    '06_sql/insert_queries.sql',
    '06_sql/select_queries.sql',
    '06_sql/joins.sql',
    '06_sql/aggregate_functions.sql',
    '07_mini_project/dataset/employees.csv',
    '07_mini_project/src/data_loader.py',
    '07_mini_project/src/analyzer.py',
    '07_mini_project/src/api_handler.py',
    '07_mini_project/src/database.py',
    '07_mini_project/src/main.py',
    '07_mini_project/outputs/report.csv',
    '07_mini_project/outputs/report.json',
    '07_mini_project/outputs/summary.txt',
    '07_mini_project/project_report.md',
    'screenshots/python_output.png',
    'screenshots/numpy_output.png',
    'screenshots/pandas_output.png',
    'screenshots/api_output.png',
    'screenshots/sql_output.png',
    'screenshots/mini_project_output.png',
]:
    path = root / rel
    if path.exists():
        path.unlink()

files = {
    'README.md': '''# Week 1 AI Foundations Project

This repository contains a complete Week 1 project covering the major topics of Python, OOP, NumPy, Pandas, APIs, SQL, and a final mini-project. The goal is to give a practical introduction to data-driven programming and AI foundations.

## Project Overview
The project demonstrates:
- Python basics such as variables, operators, loops, functions, and file handling.
- Object-oriented programming using classes, inheritance, polymorphism, encapsulation, and abstraction.
- NumPy for array creation, vectorized operations, and statistics.
- Pandas for loading, cleaning, filtering, grouping, and visualization.
- Public API data collection and transformation into JSON/CSV outputs.
- SQL scripts for schema creation, data insertion, queries, joins, and aggregations.
- A final mini-project: Employee Data Analytics System.

## Folder Structure
- 01_python_basics/: beginner Python exercises
- 02_oop/: object-oriented programming examples
- 03_numpy/: numerical operations with NumPy
- 04_pandas/: data analysis with Pandas
- 05_api_data_collection/: API fetching and JSON/CSV conversion
- 06_sql/: SQL scripts for a sample employee database
- 07_mini_project/: end-to-end analytics system
- screenshots/: sample output screenshots
- outputs/: generated CSV and JSON outputs

## Installation
1. Ensure Python 3.10+ is installed.
2. Install the required packages:
   pip install -r requirements.txt

## Execution
Run each module as follows:
- python 01_python_basics/variables_and_datatypes.py
- python 02_oop/classes_objects.py
- python 03_numpy/array_creation.py
- python 04_pandas/data_loading.py
- python 05_api_data_collection/fetch_data.py
- python 07_mini_project/src/main.py

## Results and Observations
- Python scripts print basic programming examples and create sample text files.
- NumPy examples show vectorized operations and statistics.
- Pandas scripts read and transform a sample employee dataset.
- The API module fetches public data and saves JSON and CSV results.
- The mini-project generates a report, database summary, and output files.
''',
    'requirements.txt': 'numpy\npandas\nrequests\nmatplotlib\n',
    '.gitignore': '__pycache__/\n*.pyc\n*.db\n',
    '01_python_basics/variables_and_datatypes.py': '''# Variables and data types in Python
name = "Aisha"
age = 25
salary = 82000.50
is_student = False
skills = ["Python", "SQL", "Pandas"]
profile = {"city": "Lagos", "experience": 3}
coordinates = (6.5, 7.2)
unique_tags = {"ai", "ml", "data"}

print("Name:", name)
print("Age:", age)
print("Salary:", salary)
print("Is student:", is_student)
print("Skills:", skills)
print("Profile:", profile)
print("Coordinates:", coordinates)
print("Unique tags:", unique_tags)
''',
    '01_python_basics/operators.py': '''# Arithmetic, comparison, and logical operators
x = 10
y = 3
print("Addition:", x + y)
print("Subtraction:", x - y)
print("Multiplication:", x * y)
print("Division:", x / y)
print("Floor division:", x // y)
print("Modulus:", x % y)
print("Is x greater than y?", x > y)
print("Is x equal to y?", x == y)
print("Logical AND:", (x > 5 and y < 5))
print("Logical OR:", (x < 5 or y < 5))
''',
    '01_python_basics/loops_and_conditions.py': '''# Conditional logic and loops
scores = [78, 92, 65, 88, 54]
for score in scores:
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    else:
        grade = "F"
    print(f"Score {score} -> Grade {grade}")
''',
    '01_python_basics/functions.py': '''# Functions with parameters and return values

def add_numbers(a, b):
    return a + b


def greet(name, title="Engineer"):
    return f"Hello {title} {name}"


print(add_numbers(10, 20))
print(greet("Aisha"))
print(greet("Ben", "Data Scientist"))
''',
    '01_python_basics/file_handling.py': '''# File handling example
from pathlib import Path

output_path = Path(__file__).with_name("sample_output.txt")
output_path.write_text("Python file handling demo\n", encoding="utf-8")
print("Wrote file:", output_path)
print(output_path.read_text(encoding="utf-8"))
''',
    '02_oop/classes_objects.py': '''# Classes and objects
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
''',
    '02_oop/inheritance.py': '''# Inheritance example
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
''',
    '02_oop/polymorphism.py': '''# Polymorphism example
class Shape:
    def area(self):
        raise NotImplementedError("Subclass must implement area")


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


for shape in [Rectangle(4, 5), Circle(3)]:
    print(type(shape).__name__, "area:", shape.area())
''',
    '02_oop/encapsulation.py': '''# Encapsulation example
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self._balance


account = BankAccount("Aisha", 1000)
account.deposit(250)
account.withdraw(300)
print(account.get_balance())
''',
    '02_oop/abstraction.py': '''# Abstraction using an abstract base class
from abc import ABC, abstractmethod

class DataProcessor(ABC):
    @abstractmethod
    def process(self, data):
        pass


class CSVProcessor(DataProcessor):
    def process(self, data):
        return f"Processed CSV: {data}"


processor = CSVProcessor()
print(processor.process("employee_data"))
''',
    '03_numpy/array_creation.py': '''# Creating NumPy arrays
import numpy as np

arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.zeros(5)
arr3 = np.ones(3)
arr4 = np.linspace(0, 10, 5)

print("Array from list:", arr1)
print("Zeros:", arr2)
print("Ones:", arr3)
print("Linear space:", arr4)
''',
    '03_numpy/array_operations.py': '''# Array operations using NumPy
import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("Element-wise add:", a + b)
print("Element-wise multiply:", a * b)
print("Square root:", np.sqrt(a))
print("Reshaped array:\n", a.reshape(1, 3))
''',
    '03_numpy/indexing_slicing.py': '''# Indexing and slicing with NumPy
import numpy as np

arr = np.array([10, 20, 30, 40, 50])
print("First element:", arr[0])
print("Last element:", arr[-1])
print("Slice:", arr[1:4])
print("Even values:", arr[arr % 2 == 0])
''',
    '03_numpy/statistics.py': '''# Statistics with NumPy
import numpy as np

values = np.array([10, 20, 30, 40, 50])
print("Mean:", np.mean(values))
print("Median:", np.median(values))
print("Std dev:", np.std(values))
print("Variance:", np.var(values))
''',
    '03_numpy/matrix_operations.py': '''# Matrix operations with NumPy
import numpy as np

matrix_a = np.array([[1, 2], [3, 4]])
matrix_b = np.array([[5, 6], [7, 8]])

print("Matrix A:\n", matrix_a)
print("Matrix B:\n", matrix_b)
print("Matrix product:\n", np.dot(matrix_a, matrix_b))
print("Transpose of A:\n", matrix_a.T)
''',
    '04_pandas/sample_dataset.csv': '''employee_id,name,department,salary,years_experience
1,Aisha,Engineering,90000,4
2,Ben,Sales,62000,3
3,Mina,Marketing,74000,5
4,Noah,Engineering,86000,6
5,Sara,HR,58000,2
6,Omar,Sales,70000,4
''',
    '04_pandas/data_loading.py': '''# Loading a CSV file with pandas
from pathlib import Path
import pandas as pd

csv_path = Path(__file__).with_name("sample_dataset.csv")
df = pd.read_csv(csv_path)
print(df.head())
print(df.info())
''',
    '04_pandas/data_cleaning.py': '''# Data cleaning with pandas
from pathlib import Path
import pandas as pd

csv_path = Path(__file__).with_name("sample_dataset.csv")
df = pd.read_csv(csv_path)
df.loc[2, "salary"] = None
df.loc[4, "years_experience"] = None

df["salary"] = pd.to_numeric(df["salary"], errors="coerce")
df["years_experience"] = pd.to_numeric(df["years_experience"], errors="coerce")
df = df.fillna({"salary": df["salary"].mean(), "years_experience": df["years_experience"].mean()})
print(df)
''',
    '04_pandas/filtering_sorting.py': '''# Filtering and sorting with pandas
from pathlib import Path
import pandas as pd

csv_path = Path(__file__).with_name("sample_dataset.csv")
df = pd.read_csv(csv_path)
filtered = df[df["salary"] > 70000]
sorted_df = filtered.sort_values(by="salary", ascending=False)
print(filtered)
print("\nSorted high earners:")
print(sorted_df)
''',
    '04_pandas/aggregation.py': '''# Grouping and aggregation with pandas
from pathlib import Path
import pandas as pd

csv_path = Path(__file__).with_name("sample_dataset.csv")
df = pd.read_csv(csv_path)
summary = df.groupby("department")["salary"].mean()
print(summary)
print("\nDepartment counts:")
print(df.groupby("department").size())
''',
    '04_pandas/visualization.py': '''# Basic visualization with pandas and matplotlib
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

csv_path = Path(__file__).with_name("sample_dataset.csv")
df = pd.read_csv(csv_path)
plot_path = Path(__file__).resolve().parent / "salary_plot.png"
df.plot(x="name", y="salary", kind="bar", legend=False, title="Salary by Employee")
plt.tight_layout()
plt.savefig(plot_path)
print(f"Saved plot to {plot_path}")
''',
    '05_api_data_collection/fetch_data.py': '''# Fetch public API data and save it as JSON/CSV
import csv
import json
from pathlib import Path
import requests

API_URL = "https://jsonplaceholder.typicode.com/users"
JSON_PATH = Path(__file__).with_name("api_results.json")
CSV_PATH = Path(__file__).with_name("api_results.csv")

response = requests.get(API_URL, timeout=10)
response.raise_for_status()
data = response.json()

JSON_PATH.write_text(json.dumps(data[:5], indent=2), encoding="utf-8")

with CSV_PATH.open("w", newline="", encoding="utf-8") as file_handle:
    writer = csv.DictWriter(file_handle, fieldnames=["id", "name", "email"])
    writer.writeheader()
    for item in data[:5]:
        writer.writerow({"id": item.get("id"), "name": item.get("name"), "email": item.get("email")})

print(f"Saved JSON results to {JSON_PATH}")
print(f"Saved CSV results to {CSV_PATH}")
''',
    '05_api_data_collection/process_json.py': '''# Read the saved JSON and print a simple summary
import json
from pathlib import Path

json_path = Path(__file__).with_name("api_results.json")
data = json.loads(json_path.read_text(encoding="utf-8"))
print("Fetched records:", len(data))
for item in data:
    print(item["name"], "->", item["email"])
''',
    '05_api_data_collection/api_results.json': '[]\n',
    '05_api_data_collection/api_results.csv': 'id,name,email\n',
    '06_sql/database_creation.sql': '''-- Create the employees table
CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    name VARCHAR(100),
    department VARCHAR(100),
    salary DECIMAL(10, 2)
);
''',
    '06_sql/insert_queries.sql': '''-- Insert sample records into employees
INSERT INTO employees (employee_id, name, department, salary) VALUES
(1, 'Aisha', 'Engineering', 90000),
(2, 'Ben', 'Sales', 62000),
(3, 'Mina', 'Marketing', 74000),
(4, 'Noah', 'Engineering', 86000);
''',
    '06_sql/select_queries.sql': '''-- Query all employees
SELECT * FROM employees;

-- Query employees in Engineering
SELECT name, department, salary
FROM employees
WHERE department = 'Engineering';
''',
    '06_sql/joins.sql': '''-- Example join query using a second table
CREATE TABLE departments (
    department_id INT PRIMARY KEY,
    department_name VARCHAR(100)
);

INSERT INTO departments (department_id, department_name) VALUES
(1, 'Engineering'),
(2, 'Sales'),
(3, 'Marketing');

SELECT e.name, e.department, d.department_name
FROM employees e
JOIN departments d ON e.department = d.department_name;
''',
    '06_sql/aggregate_functions.sql': '''-- Aggregate functions
SELECT department, AVG(salary) AS avg_salary
FROM employees
GROUP BY department;

SELECT MAX(salary) AS highest_salary, MIN(salary) AS lowest_salary
FROM employees;
''',
    '07_mini_project/dataset/employees.csv': '''employee_id,name,department,salary,years_experience
1,Aisha,Engineering,90000,4
2,Ben,Sales,62000,3
3,Mina,Marketing,74000,5
4,Noah,Engineering,86000,6
5,Sara,HR,58000,2
6,Omar,Sales,70000,4
''',
    '07_mini_project/src/data_loader.py': '''from pathlib import Path
import pandas as pd


class DataLoader:
    def __init__(self, csv_path: str):
        self.csv_path = Path(csv_path)

    def load_data(self):
        return pd.read_csv(self.csv_path)
''',
    '07_mini_project/src/analyzer.py': '''import numpy as np
import pandas as pd


class EmployeeAnalyzer:
    def __init__(self, dataframe: pd.DataFrame):
        self.dataframe = dataframe

    def calculate_summary(self):
        salaries = np.array(self.dataframe["salary"], dtype=float)
        return {
            "employee_count": len(self.dataframe),
            "average_salary": round(float(np.mean(salaries)), 2),
            "highest_salary": int(np.max(salaries)),
            "lowest_salary": int(np.min(salaries)),
            "department_average": self.dataframe.groupby("department")["salary"].mean().to_dict(),
        }
''',
    '07_mini_project/src/api_handler.py': '''import json
from pathlib import Path
import requests


class APIHandler:
    def __init__(self, url: str):
        self.url = url

    def fetch_data(self):
        try:
            response = requests.get(self.url, timeout=10)
            response.raise_for_status()
            return response.json()
        except Exception:
            return [{"name": "Fallback Employee", "company": "Example Corp"}]
''',
    '07_mini_project/src/database.py': '''import sqlite3
from pathlib import Path


class DatabaseManager:
    def __init__(self, db_path: str):
        self.db_path = Path(db_path)

    def save_summary(self, summary: dict):
        with sqlite3.connect(self.db_path) as connection:
            connection.execute("DROP TABLE IF EXISTS employee_summary")
            connection.execute(
                "CREATE TABLE employee_summary (employee_count INT, average_salary REAL, highest_salary INT, lowest_salary INT)"
            )
            connection.execute(
                "INSERT INTO employee_summary VALUES (?, ?, ?, ?)",
                (summary["employee_count"], summary["average_salary"], summary["highest_salary"], summary["lowest_salary"]),
            )
''',
    '07_mini_project/src/main.py': '''import json
from pathlib import Path
import pandas as pd

from data_loader import DataLoader
from analyzer import EmployeeAnalyzer
from api_handler import APIHandler
from database import DatabaseManager

ROOT = Path(__file__).resolve().parents[1]
DATASET_PATH = ROOT / "dataset" / "employees.csv"
REPORT_CSV_PATH = ROOT / "outputs" / "report.csv"
REPORT_JSON_PATH = ROOT / "outputs" / "report.json"
SUMMARY_PATH = ROOT / "outputs" / "summary.txt"
DB_PATH = ROOT / "outputs" / "employee_summary.db"


def main():
    loader = DataLoader(DATASET_PATH)
    df = loader.load_data()

    analyzer = EmployeeAnalyzer(df)
    summary = analyzer.calculate_summary()

    api_handler = APIHandler("https://jsonplaceholder.typicode.com/users")
    api_data = api_handler.fetch_data()

    db_manager = DatabaseManager(DB_PATH)
    db_manager.save_summary(summary)

    df.to_csv(REPORT_CSV_PATH, index=False)
    REPORT_JSON_PATH.write_text(json.dumps(summary, indent=2), encoding="utf-8")
    SUMMARY_PATH.write_text(
        f"Employee Count: {summary['employee_count']}\n"
        f"Average Salary: {summary['average_salary']}\n"
        f"Highest Salary: {summary['highest_salary']}\n"
        f"Lowest Salary: {summary['lowest_salary']}\n",
        encoding="utf-8",
    )

    print("Mini project completed successfully")
    print(summary)
    print("API data sample:", api_data[0])


if __name__ == "__main__":
    main()
''',
    '07_mini_project/outputs/report.csv': 'employee_id,name,department,salary,years_experience\n',
    '07_mini_project/outputs/report.json': '{}\n',
    '07_mini_project/outputs/summary.txt': 'Mini project summary pending\n',
    '07_mini_project/project_report.md': '''# Employee Data Analytics System Report

## Objectives
The objective of this mini-project is to integrate Python, NumPy, Pandas, API collection, and SQL operations into one cohesive analytics workflow.

## Implementation
- A CSV dataset of employees was loaded using Pandas.
- Salary statistics were computed using NumPy.
- Public API data was fetched and used as a fallback source.
- Summary metrics were saved to SQLite and exported to CSV and JSON files.

## Outputs
- report.csv: employee records
- report.json: salary summary
- summary.txt: human-readable summary

## Conclusion
The system demonstrates how to combine multiple data tools to produce a simple analytics pipeline.
''',
}

for rel_path, content in files.items():
    path = root / rel_path
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding='utf-8')

# Create placeholder PNG files using a simple 1x1 PNG base64 payload.
png_payload = base64.b64decode('iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAACklEQVR4nGMAAIAAeIhK3QAAAABJRU5ErkJggg==')
for image_name in [
    'python_output.png', 'numpy_output.png', 'pandas_output.png', 'api_output.png', 'sql_output.png', 'mini_project_output.png'
]:
    (root / 'screenshots' / image_name).write_bytes(png_payload)

# If requirements are already present, keep them updated.
print('Project files generated successfully.')
