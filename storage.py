import json
from pathlib import Path
FILE = Path("scores.json")

def load_scores():
    if not FILE.exists():
        return {}
    try:
        return json.loads(FILE.read_text())
    except (json.JSONDecodeError, OSError):
        return {}

def save_scores(data):
    FILE.write_text(json.dumps(data, indent=2))
