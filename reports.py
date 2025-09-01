from colorama import Fore, Style

GREEN = Fore.GREEN
RED = Fore.RED
CYAN = Fore.CYAN
YELLOW = Fore.YELLOW
RESET = Style.RESET_ALL

def summary_report(transactions):
    """Show summary of income, expenses, and balance"""
    total_income = 0
    total_expense = 0
    category_expenses = {}

    for t in transactions:
        amount = float(t["amount"])
        if t["type"] == "income":
            total_income += amount
        else:
            total_expense += amount
            category_expenses[t["category"]] = category_expenses.get(t["category"], 0) + amount

    balance = total_income - total_expense

    print("\n=== Summary Report ===")
    print(f"Total Income : {GREEN}RM{total_income:.2f}{RESET}")
    print(f"Total Expense: {RED}RM{total_expense:.2f}{RESET}")
    print(f"Balance      : {CYAN}RM{balance:.2f}{RESET}")
    print("\nExpenses by Category:")
    for cat, amt in category_expenses.items():
        print(f"{YELLOW}  {cat}: RM{amt:.2f}{RESET}")
    print("----------------------\n")
