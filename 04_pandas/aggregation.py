# Grouping and aggregation with pandas
from pathlib import Path
import pandas as pd

csv_path = Path(__file__).with_name("sample_dataset.csv")
df = pd.read_csv(csv_path)
summary = df.groupby("department")["salary"].mean()
print(summary)
print("
Department counts:")
print(df.groupby("department").size())
