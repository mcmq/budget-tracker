import csv
from datetime import datetime
from colorama import Fore, Style

FILENAME = "budget_data.csv"

GREEN = Fore.GREEN
RED = Fore.RED
CYAN = Fore.CYAN
YELLOW = Fore.YELLOW
RESET = Style.RESET_ALL

def load_transactions():
    """Load transactions from CSV file"""
    transactions = []
    try:
        with open(FILENAME, mode="r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                transactions.append(row)
    except FileNotFoundError:
        pass
    return transactions


def save_transactions(transactions):
    """Save transactions to CSV file"""
    with open(FILENAME, mode="w", newline="") as file:
        fieldnames = ["date", "type", "category", "amount"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for t in transactions:
            writer.writerow(t)


def add_transaction(transactions):
    """Add income or expense transaction"""

    print(Fore.CYAN + "Select transaction type:" + Style.RESET_ALL)
    print("1. Income")
    print("2. Expense")

    choice = input("Enter choice (1/2): ").strip()

    if choice == "1":
        t_type = "income"
        categories = ["Salary", "Gift", "Investment", "Other"]
    elif choice == "2":
        t_type = "expense"
        categories = ["Food", "Transport", "Bills", "Entertainment", "Other"]
    else:
        print(Fore.RED + "❌ Invalid choice!" + Style.RESET_ALL)
        return

    print(Fore.CYAN + f"Select {t_type} category:" + Style.RESET_ALL)
    for i, cat in enumerate(categories, 1):
        print(f"{i}. {cat}")

    try:
        cat_choice = int(input("Enter choice: "))
        if not (1 <= cat_choice <= len(categories)):
            raise ValueError
        category = categories[cat_choice - 1]
    except ValueError:
        print(Fore.RED + "❌ Invalid category choice!" + Style.RESET_ALL)
        return

    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print(Fore.RED + "❌ Invalid amount! Must be a number." + Style.RESET_ALL)
        return

    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    transactions.append({
        "date": date,
        "type": t_type,
        "category": category,
        "amount": str(amount)
    })

    save_transactions(transactions)
    print(Fore.GREEN + "✅ Transaction added successfully!" + Style.RESET_ALL)

def view_transactions(transactions):
    """Display all transactions with colors"""
    if not transactions:
        print("No transactions found.")
        return

    print("\n=== All Transactions ===")
    for t in transactions:
        amount = f"RM{t['amount']}"
        if t["type"] == "income":
            amount = GREEN + "+ " + amount + RESET
        else:
            amount = RED + "- " + amount + RESET

        print(
            f"{t['type'].capitalize():<8} | "
            f"{YELLOW}{t['date']:<10}{RESET} | "
            f"{CYAN}{t['category']:<13}{RESET} | "
            f"{amount}"
        )
    print("------------------------\n")
