import sqlite3
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
