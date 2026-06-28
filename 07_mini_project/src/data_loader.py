from pathlib import Path
import pandas as pd


class DataLoader:
    def __init__(self, csv_path: str):
        self.csv_path = Path(csv_path)

    def load_data(self):
        return pd.read_csv(self.csv_path)
