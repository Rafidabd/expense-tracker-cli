# Expense Tracker CLI

I built this while learning Python because I wanted to make something that did more than print an answer and exit. Recording expenses seemed like a good place to start: I needed to save information, check user input, and do something useful with the records afterwards.

It runs entirely in the terminal. It's a small project, but it was one of my first attempts at splitting a program into several files instead of putting everything in `main.py`.

## What it can do

- Add an expense with a title, amount, category, and date.
- Show all saved expenses and remove one by its ID.
- Calculate total spending and totals for each category.
- Filter the list by category.
- Save expenses in a local JSON file, so they stay there after the program closes.

At the moment, amounts have to be positive whole numbers, dates use `YYYY-MM-DD`, and categories come from [`config/categories.json`](config/categories.json).

## A look at the program

| Menu | Expense list |
| --- | --- |
| ![Menu](assets/menu.png) | ![Expenses](assets/expenses.png) |

Here's the category summary:

![Category summary](assets/analytics.png)

## Run it yourself

You only need Python 3; there are no external packages to install.

```bash
git clone https://github.com/Rafidabd/expense-tracker-cli.git
cd expense-tracker-cli
python main.py
```

The program creates `data/expenses.json` the first time it needs it. The file stays inside the project folder and is ignored by Git.

An example record looks like this (this is fictional data):

```json
{
  "id": "E001",
  "title": "Lunch",
  "amount": 250,
  "category": "Food",
  "date": "2026-03-10"
}
```

## How I organized it

```text
expense-tracker-cli/
├── assets/             # Screenshots for this README
├── config/
│   └── categories.json
├── modules/
│   ├── analytics.py    # Spending calculations and filters
│   ├── cli.py          # Terminal menu
│   ├── config_loader.py
│   ├── display.py      # Output formatting
│   ├── expense_manager.py
│   └── storage.py      # JSON files and expense IDs
├── tests/
│   └── test_storage.py
├── main.py
└── README.md
```

One useful lesson from this project was that deciding where to put the files matters. I initially tied the JSON path to the folder I was running Python from. When I moved the project into its own repository, I fixed that so the data location is based on the project's files instead.

## Tests

From the project folder:

```bash
python -m unittest discover -s tests -v
```

There are three small tests covering an empty store, adding and deleting an expense, and rejecting an invalid amount. The tests use temporary files and don't touch your expenses. They don't cover every menu option yet.

## What I'd improve

This is a learning project, not personal-finance software. It has no accounts, database, or synchronization between devices. I'd also like to make expense ID generation more robust and add more tests for invalid inputs.

I originally built it inside [my Python practice repository](https://github.com/Rafidabd/python-phase-1/tree/main/day13_Mini_Projects/expense-tracker-cli). I later moved it here while keeping its project-specific commit history, so the earlier stages are still visible.
