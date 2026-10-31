##import csv
##import os
##from datetime import datetime
##import pandas as pd
##
##FILE_NAME = "expenses.csv"
##
### Create CSV file if it doesn't exist
##if not os.path.exists(FILE_NAME):
##    with open(FILE_NAME, "w", newline="") as file:
##        writer = csv.writer(file)
##        writer.writerow(["Date", "Category", "Description", "Amount"])
##
##
##def validate_date(date):
##    try:
##        datetime.strptime(date, "%Y-%m-%d")
##        return True
##    except:
##        return False
##
##
##def add_expense():
##    date = input("Enter Date (YYYY-MM-DD): ")
##
##    if not validate_date(date):
##        print("Invalid date format!")
##        return
##
##    category = input("Enter Category: ")
##    description = input("Enter Description: ")
##
##    try:
##        amount = float(input("Enter Amount: "))
##    except:
##        print("Invalid amount. Amount must be a positive number. Expense not saved.")
##        return
##
##    if amount <= 0:
##        print("Invalid amount. Amount must be a positive number. Expense not saved.")
##        return
##
##    with open(FILE_NAME, "a", newline="") as file:
##        writer = csv.writer(file)
##        writer.writerow([date, category, description, amount])
##
##    df = pd.read_csv(FILE_NAME)
##    print(f"Expense saved. Total records: {len(df)}")
##
##
##def view_expenses():
##    df = pd.read_csv(FILE_NAME)
##
##    if df.empty:
##        print("No expenses found.")
##    else:
##        print("\nAll Expenses")
##        print(df)
##
##
##def category_summary():
##    df = pd.read_csv(FILE_NAME)
##
##    if df.empty:
##        print("No expenses found.")
##        return
##
##    summary = df.groupby("Category")["Amount"].sum()
##
##    print("\nCategory Summary")
##    for category, amount in summary.items():
##        if amount == int(amount):
##            amount = int(amount)
##        print(f"{category}: {amount}")
##
##    total = df["Amount"].sum()
##    if total == int(total):
##        total = int(total)
##    print(f"Total: {total}")
##
##
##def monthly_summary():
##    df = pd.read_csv(FILE_NAME)
##
##    if df.empty:
##        print("No expenses found.")
##        return
##
##    df["Month"] = pd.to_datetime(df["Date"]).dt.strftime("%Y-%m")
##    summary = df.groupby("Month")["Amount"].sum()
##
##    print("\nMonthly Summary")
##    print(summary)
##
##
##while True:
##    print("\n========== PERSONAL EXPENSE TRACKER ==========")
##    print("1. Add Expense")
##    print("2. View Expenses")
##    print("3. Category Summary")
##    print("4. Monthly Summary")
##    print("5. Exit")
##
##    choice = input("Enter Choice: ")
##
##    if choice == "1":
##        add_expense()
##
##    elif choice == "2":
##        view_expenses()
##
##    elif choice == "3":
##        category_summary()
##
##    elif choice == "4":
##        monthly_summary()
##
##    elif choice == "5":
##        print("Thank You!")
##        break
##
##    else:
##        print("Invalid Choice!")










import csv
import os
from datetime import datetime
import pandas as pd

FILE_NAME = "expenses.csv"

# Create CSV file if it doesn't exist
if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Category", "Description", "Amount"])


# ---------------- VALIDATE DATE ----------------
def validate_date(date):
    try:
        datetime.strptime(date, "%Y-%m-%d")
        return True
    except:
        return False


# ---------------- ADD EXPENSE ----------------
def add_expense():
    date = input("Enter Date (YYYY-MM-DD): ")

    if not validate_date(date):
        print("Invalid date format!")
        return

    category = input("Enter Category: ")
    description = input("Enter Description: ")

    try:
        amount = float(input("Enter Amount: "))
    except:
        print("Invalid amount. Amount must be a positive number. Expense not saved.")
        return

    if amount <= 0:
        print("Invalid amount. Amount must be a positive number. Expense not saved.")
        return

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, description, amount])

    df = pd.read_csv(FILE_NAME)
    print(f"\nExpense saved. Total records: {len(df)}")


# ---------------- VIEW EXPENSES ----------------
def view_expenses():
    df = pd.read_csv(FILE_NAME)

    if df.empty:
        print("\nNo expenses found.")
    else:
        print("\n========== ALL EXPENSES ==========")
        print(df.to_string(index=False))


# ---------------- DELETE ALL EXPENSES ----------------
def delete_all_expenses():
    df = pd.read_csv(FILE_NAME)

    if df.empty:
        print("\nNo expenses found.")
        return

    confirm = input(
        "Are you sure you want to delete ALL expenses? (yes/no): "
    ).strip().lower()

    if confirm == "yes":
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Description", "Amount"])

        print("\nAll expenses have been deleted successfully!")
    else:
        print("\nOperation cancelled.")


# ---------------- CATEGORY SUMMARY ----------------
def category_summary():
    df = pd.read_csv(FILE_NAME)

    if df.empty:
        print("\nNo expenses found.")
        return

    summary = df.groupby("Category")["Amount"].sum()

    print("\n========== CATEGORY SUMMARY ==========")

    for category, amount in summary.items():
        if amount == int(amount):
            amount = int(amount)
        print(f"{category}: {amount}")

    total = df["Amount"].sum()

    if total == int(total):
        total = int(total)

    print(f"Total: {total}")


# ---------------- MONTHLY SUMMARY ----------------
def monthly_summary():
    df = pd.read_csv(FILE_NAME)

    if df.empty:
        print("\nNo expenses found.")
        return

    df["Month"] = pd.to_datetime(df["Date"]).dt.strftime("%Y-%m")

    summary = df.groupby("Month")["Amount"].sum()

    print("\n========== MONTHLY SUMMARY ==========")

    for month, amount in summary.items():
        if amount == int(amount):
            amount = int(amount)
        print(f"{month}: {amount}")


# ---------------- MAIN MENU ----------------
while True:

    print("\n==========================================")
    print("      PERSONAL EXPENSE TRACKER")
    print("==========================================")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Category Summary")
    print("4. Monthly Summary")
    print("5. Delete All Expenses")
    print("6. Exit")
    print("==========================================")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        category_summary()

    elif choice == "4":
        monthly_summary()

    elif choice == "5":
        delete_all_expenses()

    elif choice == "6":
        print("\nThank you for using Personal Expense Tracker!")
        break

    else:
        print("\nInvalid choice! Please try again.")
        
