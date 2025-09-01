# 💰 Personal Finance Tracker (CLI)

A simple **command-line finance tracker** written in **Python** that lets you record **income** and **expenses**, categorize them, and view colorful reports directly in your terminal.



## ✨ Features
- Add **Income** and **Expense** transactions
- Choose from predefined categories (different for income & expense)
- Colorful terminal output:
  - 🟢 Green for Income
  - 🔴 Red for Expense
- View all transactions with neat formatting
- Easy-to-use number-based menu



## 🚀 Installation & Setup

1. Make sure you have **Python 3** installed:
   ```
   python3 --version
   ```
   
2. Clone or download this project:
   ```
   git clone https://github.com/yourusername/finance-tracker.git
   cd finance-tracker
   ```

3. Run the app:
   ```
   python3 main.py
   ```

## 📖 Usage Guide

When you run the app, you will see a menu like this:

### 📌 Finance Tracker
1. Add Income
2. Add Expense
3. View Transactions
4. Exit

### 1️⃣ Adding Income

If you choose 1 (Add Income):

Select Income Category:
1. Salary
2. Business
3. Gift
4. Other

**Then enter the amount.**

Example:
   ```
   Added income: Salary | RM5000
   ```

2️⃣ Adding Expense

If you choose 2 (Add Expense):

Select Expense Category:
1. Food
2. Rent
3. Transport
4. Entertainment
5. Other


**Then enter the amount.**

Example:
```
   Added expense: Food | RM20
```

### 3️⃣ Viewing Transactions

When you select 3 (View Transactions), you’ll see a colorful list:

```
=== All Transactions ===
Income  | 2025-09-01 | Salary       | RM5000   (🟢 Green)
Expense | 2025-09-01 | Food         | RM20     (🔴 Red)
Expense | 2025-09-02 | Transport    | RM10     (🔴 Red)
Income  | 2025-09-03 | Business     | RM1200   (🟢 Green)
------------------------
```

## 📌 Future Improvements

1. Save data to a file (CSV / JSON)

2. Monthly reports

3. Balance summary

4. Export to Excel/PDF

## 👨‍💻 Author

Developed by **Mohamed Abdillahi**