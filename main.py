import os
import json

list_of_expense = []
FILE_NAME = "tracks.json"


def expense_track(expenses):
    try:
        amount = float(input("Enter the amount: "))

        if amount <= 0:
            print("Amount must be greater than zero.")
            return

        category = input("Enter the category: ")
        description = input("Enter the description: ")

        expense = {
            "amount": amount,
            "category": category,
            "description": description
        }

        expenses.append(expense)

        # Save all expenses to the file
        with open(FILE_NAME, "w") as file:
            json.dump(expenses, file, indent=4)

        print("Expense added successfully!")

    except ValueError:
        print("Invalid amount! Please enter a number.")

    except OSError as error:
        print("File error:", error)


# Load previously saved expenses
if os.path.exists(FILE_NAME):
    try:
        with open(FILE_NAME, "r") as file:
            list_of_expense = json.load(file)
    except (OSError, json.JSONDecodeError):
        print("Couldn't load saved expenses. Starting with an empty list.")
        list_of_expense = []


# Main menu
while True:
    print("\n====== EXPENSE TRACKER ======")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Show Total Spending")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        expense_track(list_of_expense)

    elif choice == "2":
        if len(list_of_expense) == 0:
            print("No expenses recorded yet.")
        else:
            for expense in list_of_expense:
                print("\nAmount:", expense["amount"])
                print("Category:", expense["category"])
                print("Description:", expense["description"])

    elif choice == "3":
        total = 0

        for expense in list_of_expense:
            total += expense["amount"]

        print(f"Total spending: ₹{total:.2f}")

    elif choice == "4":
        print("Exiting Expense Tracker. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
