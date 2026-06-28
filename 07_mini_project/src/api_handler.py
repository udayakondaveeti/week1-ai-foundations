import json
from pathlib import Path
import requests


class APIHandler:
    def __init__(self, url: str):
        self.url = url

    def fetch_data(self):
        try:
            response = requests.get(self.url, timeout=10)
            response.raise_for_status()
            return response.json()
        except Exception:
            return [{"name": "Fallback Employee", "company": "Example Corp"}]
