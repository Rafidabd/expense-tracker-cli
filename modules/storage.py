"""JSON-backed storage for local expense records."""

import json
from pathlib import Path

# Resolve the data file relative to this standalone project, not the shell's CWD.
PROJECT_DIR = Path(__file__).resolve().parent.parent
EXPENSE_FILE = PROJECT_DIR / "data" / "expenses.json"


def load_expenses():
    EXPENSE_FILE.parent.mkdir(parents=True, exist_ok=True)

    if not EXPENSE_FILE.exists():
        EXPENSE_FILE.write_text("[]", encoding="utf-8")

    try:
        with EXPENSE_FILE.open("r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []


def save_expenses(expenses):
    EXPENSE_FILE.parent.mkdir(parents=True, exist_ok=True)

    with EXPENSE_FILE.open("w", encoding="utf-8") as f:
        json.dump(expenses, f, indent=4)


def generate_expense_id(expenses):
    if not expenses:
        return "E001"

    last_id = expenses[-1]["id"]
    last_number = int(last_id[1:])
    return f"E{last_number + 1:03}"
