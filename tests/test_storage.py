"""Focused storage and expense workflow tests using temporary JSON files."""

import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from modules import storage
from modules.expense_manager import add_expense, delete_expense, get_all_expenses


class ExpenseStorageTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp_dir.cleanup)
        data_file = Path(self.temp_dir.name) / "data" / "expenses.json"
        path_override = patch.object(storage, "EXPENSE_FILE", data_file)
        path_override.start()
        self.addCleanup(path_override.stop)

    def test_first_load_creates_empty_store(self):
        self.assertEqual(get_all_expenses(), [])
        self.assertTrue(storage.EXPENSE_FILE.exists())

    def test_add_and_delete_expense(self):
        result = add_expense("Lunch", "250", "Food", "2026-03-10")
        self.assertEqual(result["status"], "success")
        records = get_all_expenses()
        self.assertEqual(len(records), 1)
        self.assertEqual(records[0]["id"], "E001")
        self.assertEqual(records[0]["amount"], 250)

        deleted = delete_expense("E001")
        self.assertEqual(deleted["status"], "success")
        self.assertEqual(get_all_expenses(), [])

    def test_invalid_amount_is_not_saved(self):
        result = add_expense("Lunch", "0", "Food", "2026-03-10")
        self.assertEqual(result["status"], "error")
        self.assertEqual(get_all_expenses(), [])


if __name__ == "__main__":
    unittest.main()
