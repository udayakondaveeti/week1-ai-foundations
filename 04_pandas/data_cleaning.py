# Data cleaning with pandas
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
