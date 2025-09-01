from transactions import load_transactions, add_transaction, view_transactions
from reports import summary_report

def main():
    transactions = load_transactions()

    while True:
        print("\n=== Personal Budget Tracker ===")
        print("1. Add Transaction")
        print("2. View All Transactions")
        print("3. View Summary Report")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            add_transaction(transactions)
        elif choice == "2":
            view_transactions(transactions)
        elif choice == "3":
            summary_report(transactions)
        elif choice == "4":
            print("Goodbye! 👋")
            break
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()