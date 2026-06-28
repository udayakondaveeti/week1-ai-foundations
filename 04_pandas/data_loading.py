# Loading a CSV file with pandas
from pathlib import Path
import pandas as pd

csv_path = Path(__file__).with_name("sample_dataset.csv")
df = pd.read_csv(csv_path)
print(df.head())
print(df.info())
