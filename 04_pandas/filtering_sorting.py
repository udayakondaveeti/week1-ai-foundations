# Filtering and sorting with pandas
from pathlib import Path
import pandas as pd

csv_path = Path(__file__).with_name("sample_dataset.csv")
df = pd.read_csv(csv_path)
filtered = df[df["salary"] > 70000]
sorted_df = filtered.sort_values(by="salary", ascending=False)
print(filtered)
print("
Sorted high earners:")
print(sorted_df)
