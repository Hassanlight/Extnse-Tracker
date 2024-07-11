from typing import Dict, Any

from expense import Expense


def main():
    print(f"Running Expenses Tracker")
    expense_file_path = "expenses.csv"

    # User Input for Expense
    expense = get_user_expense()



    # Write the Expenses into a File
    save_expense_to_file(expense, expense_file_path)

    # read the file and Summarize the Expenses
    summarize_expense(expense_file_path)


def get_user_expense():
    print(f"Get User input Expense")
    expense_name = input("Enter Expense Name: ")
    expense_amount = float(input("Enter Expense Amount: "))

    expense_categories = [
        "Food 😋",
        "Rent 🏠",
        "Work 👷",
        "Fun 😜",
        "Others 📛 ",

]
    while True:
        print("Select a category: ")
        for i, category_name in enumerate(expense_categories):
            print(f"  {i+1}.{category_name}")
        value_range = f"[1 - {len(expense_categories)}]"
        selected_index = int(input(f"Enter a category Number {value_range}: "))

        if 1<= selected_index <= (len(expense_categories)):
            selected_category = expense_categories[selected_index-1]
            new_expense = Expense(
                name=expense_name, category=selected_category, amount=expense_amount
            )
            return new_expense
        else:
            print("invalid Number. Please Try again.")


def save_expense_to_file(expense:Expense, expense_file_path):
    print(f"Save user expenses into a file: {expense} to {expense_file_path} ")
    with open(expense_file_path,"a", newline='',encoding='utf-8') as f:
        f.write(f"{expense.name},{expense.category},{expense.amount}\n")


def summarize_expense(expense_file_path):
    print(f"Summarize User Expenses")
    expenses = []
    with open(expense_file_path, "r", newline='',encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:

            expense_name, expense_category, expense_amount = line.strip().split(",")
            line_expense = Expense(
                name=expense_name,
                amount=float(expense_amount),
                category=expense_category,
            )
            expenses.append(line_expense)

    amount_by_category: dict[Any, Any] = {}
    for expense in expenses:
        key = expense.category
        if key in amount_by_category:
            amount_by_category[key] += expense_amount
        else:
            amount_by_category[key] = expense_amount
    print("Expenses by category 📈:")
    for key, amount in amount_by_category.items():
        print(f" {key}: ${amount:.2f}")




if __name__ == "__main__":
    main()