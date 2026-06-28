# File handling example
from pathlib import Path

output_path = Path(__file__).with_name("sample_output.txt")
output_path.write_text("Python file handling demo
", encoding="utf-8")
print("Wrote file:", output_path)
print(output_path.read_text(encoding="utf-8"))
