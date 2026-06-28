import json
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
