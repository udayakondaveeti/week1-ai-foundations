import numpy as np
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
