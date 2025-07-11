import json
from pathlib import Path

def get_questions():
    path = Path(__file__).parent / "questions.json"
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)
