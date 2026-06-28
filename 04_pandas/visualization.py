# Basic visualization with pandas and matplotlib
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
