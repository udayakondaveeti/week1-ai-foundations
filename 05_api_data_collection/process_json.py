# Read the saved JSON and print a simple summary
import json
from pathlib import Path

json_path = Path(__file__).with_name("api_results.json")
data = json.loads(json_path.read_text(encoding="utf-8"))
print("Fetched records:", len(data))
for item in data:
    print(item["name"], "->", item["email"])
