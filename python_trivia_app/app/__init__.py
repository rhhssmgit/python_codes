from pathlib import Path

def get_version():
    version_path = Path(__file__).parent.parent / "VERSION"
    with open(version_path, "r", encoding="utf-8") as f:
        return f.read().strip()

print(f"🧠 Python Trivia Game - Version {get_version()}\n")
