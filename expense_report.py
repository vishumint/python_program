import csv
from datetime import datetime


class ExpenseTracker:
    """
    A class to represent a personal expense tracker that allows users to log, categorize,
    and track daily expenses against a monthly budget. The tracker also includes
    functionality to save and load expense data from a CSV file.

    Attributes:
    -----------
    expenses : list
        A list to store expense entries as dictionaries.
    budget : float
        The user's monthly budget for expenses.

    Methods:
    --------
    add_expense():
        Prompts user to input expense details and adds it to the expense list.
    view_expenses():
        Displays all the expenses recorded by the user.
    set_budget():
        Prompts user to set a monthly budget.
    track_budget():
        Tracks and compares the total expenses against the user's monthly budget.
    save_expenses(filename):
        Saves the list of expenses to a CSV file.
    load_expenses(filename):
        Loads expenses from a CSV file and appends to the current list of expenses.
    menu():
        Displays an interactive menu for the user to navigate through options.
    """

    def __init__(self):
        """Initialize the expense tracker with an empty list of expenses and no budget set."""
        self.expenses = []
        self.budget = 0.0

    def add_expense(self):
        """Prompt the user for expense details and add the expense to the list."""
        try:
            date = input("Enter the date of expense (YYYY-MM-DD): ")
            datetime.strptime(date, '%Y-%m-%d')  # Validates the date format
            category = input("Enter the category of expense (e.g., Food, Travel): ")
            amount = float(input("Enter the amount spent: "))
            description = input("Enter a brief description of the expense: ")

            expense = {
                'date': date,
                'category': category,
                'amount': amount,
                'description': description
            }
            self.expenses.append(expense)
            print("Expense added successfully!")
        except ValueError:
            print("Invalid input! Please try again.")

    def view_expenses(self):
        """Display all the expenses in the list."""
        if not self.expenses:
            print("No expenses to display.")
            return

        print("\nList of expenses:")
        for expense in self.expenses:
            if all(expense.values()):  # Ensure all fields are present
                print(f"Date: {expense['date']}, Category: {expense['category']}, "
                      f"Amount: {expense['amount']}, Description: {expense['description']}")
            else:
                print("Incomplete expense entry found, skipping.")
        print()

    def set_budget(self):
        """Allow the user to input a monthly budget."""
        try:
            self.budget = float(input("Enter your monthly budget: "))
            print(f"Monthly budget set to {self.budget}")
        except ValueError:
            print("Invalid budget input. Please enter a valid number.")

    def track_budget(self):
        """Compare total expenses with the monthly budget and notify the user."""
        total_expenses = sum(expense['amount'] for expense in self.expenses)
        print(f"\nTotal expenses so far: {total_expenses:.2f}")

        if total_expenses > self.budget:
            print(f"You have exceeded your budget by {total_expenses - self.budget:.2f}!")
        else:
            print(f"You have {self.budget - total_expenses:.2f} left for the month.")
        print()

    def save_expenses(self, filename='expenses.csv'):
        """Save all expenses to a CSV file."""
        try:
            with open(filename, 'w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=['date', 'category', 'amount', 'description'])
                writer.writeheader()
                writer.writerows(self.expenses)
            print(f"Expenses saved to {filename} successfully!")
        except Exception as e:
            print(f"Error saving expenses: {e}")

    def load_expenses(self, filename='expenses.csv'):
        """Load expenses from a CSV file into the current list."""
        try:
            with open(filename, 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    row['amount'] = float(row['amount'])  # Convert amount to float
                    self.expenses.append(row)
            print(f"Expenses loaded from {filename} successfully!")
        except FileNotFoundError:
            print(f"No file found: {filename}. Starting with empty expense list.")
        except Exception as e:
            print(f"Error loading expenses: {e}")

    def menu(self):
        """Display an interactive menu for the user to manage expenses and budgets."""
        while True:
            print("\nExpense Tracker Menu:")
            print("1. Add expense")
            print("2. View expenses")
            print("3. Set budget")
            print("4. Track budget")
            print("5. Save expenses")
            print("6. Load expenses")
            print("7. Exit")

            choice = input("Choose an option: ")

            if choice == '1':
                self.add_expense()
            elif choice == '2':
                self.view_expenses()
            elif choice == '3':
                self.set_budget()
            elif choice == '4':
                self.track_budget()
            elif choice == '5':
                self.save_expenses()
            elif choice == '6':
                self.load_expenses()
            elif choice == '7':
                print("Saving expenses and exiting program.")
                self.save_expenses()
                break
            else:
                print("Invalid option. Please try again.")


# Run the Expense Tracker
if __name__ == "__main__":
    tracker = ExpenseTracker()
    tracker.menu()
