# runner/loader.py

from pathlib import Path

BASE = Path(__file__).resolve().parent.parent

def load_markdown(relative_path: str) -> str:
    file_path = BASE / relative_path
    return file_path.read_text(encoding="utf-8")