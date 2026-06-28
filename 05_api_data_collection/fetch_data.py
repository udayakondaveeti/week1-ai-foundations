# Fetch public API data and save it as JSON/CSV
import csv
import json
from pathlib import Path
import requests

API_URL = "https://jsonplaceholder.typicode.com/users"
JSON_PATH = Path(__file__).with_name("api_results.json")
CSV_PATH = Path(__file__).with_name("api_results.csv")

response = requests.get(API_URL, timeout=10)
response.raise_for_status()
data = response.json()

JSON_PATH.write_text(json.dumps(data[:5], indent=2), encoding="utf-8")

with CSV_PATH.open("w", newline="", encoding="utf-8") as file_handle:
    writer = csv.DictWriter(file_handle, fieldnames=["id", "name", "email"])
    writer.writeheader()
    for item in data[:5]:
        writer.writerow({"id": item.get("id"), "name": item.get("name"), "email": item.get("email")})

print(f"Saved JSON results to {JSON_PATH}")
print(f"Saved CSV results to {CSV_PATH}")
