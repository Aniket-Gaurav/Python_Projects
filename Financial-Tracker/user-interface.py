import json
import tkinter as tk
from tkinter import messagebox

# Class to represent a transaction with description and amount
class Transaction:
    def __init__(self, description, amount):
        self.description = description
        self.amount = amount

# Main application class for the finance tracker
class FinanceTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Finance Tracker")

        # Set up labels for description and amount
        tk.Label(root, text="Description").grid(row=0, column=0)
        tk.Label(root, text="Amount").grid(row=0, column=1)

        # Entry fields for user to input transaction data
        self.desc_entry = tk.Entry(root)
        self.amount_entry = tk.Entry(root)

        # Position entry fields in the grid
        self.desc_entry.grid(row=1, column=0)
        self.amount_entry.grid(row=1, column=1)

        # Button to add a new transaction
        tk.Button(root, text="Add Transaction",
                  command=self.add_transaction).grid(row=1, column=2)

        # List to store transactions and listbox to display them
        self.transactions = []
        self.transaction_listbox = tk.Listbox(root)
        self.transaction_listbox.grid(row=2, column=0, columnspan=3)

        # Button to calculate total income and expenses
        tk.Button(root, text="Calculate Total", command=self.calculate_total).grid(
            row=3, column=0, columnspan=3)

        # Labels to display total income and expenses
        self.total_income_label = tk.Label(root, text="Total Income: Rs. 0")
        self.total_expenses_label = tk.Label(
            root, text="Total Expenses: Rs. 0")

        # Position total income and expenses labels in the grid
        self.total_income_label.grid(row=4, column=0, columnspan=2)
        self.total_expenses_label.grid(row=5, column=2)

        # Load transactions from file
        self.load_transactions()
        self.calculate_total()

    # Function to add a transaction to the list
    def add_transaction(self):
        description = self.desc_entry.get()
        amount = self.amount_entry.get()
        if description and amount:
            try:
                # Attempt to convert amount to float and add transaction
                amount = float(amount)
                self.transactions.append((description, amount))
                self.transaction_listbox.insert(
                    tk.END, f"{description}: Rs. {amount}")
                self.desc_entry.delete(0, tk.END)
                self.amount_entry.delete(0, tk.END)
            except ValueError:
                # Show error if amount is not a valid number
                messagebox.showerror(
                    "Input Error", "Please enter a valid number for amount.")
        else:
            # Show warning if either description or amount is missing
            messagebox.showwarning(
                "Input Error", "Please enter both description and amount.")

    # Function to save transactions to a JSON file
    def save_transactions(self):
        try:
            with open('transactions.json', 'w') as f:
                json.dump(self.transactions, f)
        except IOError as e:
            messagebox.showerror(
                "File Error", f"An error occurred while saving transactions: {e}")

    # Function to load transactions from a JSON file
    def load_transactions(self):
        try:
            with open('transactions.json', 'r') as f:
                self.transactions = json.load(f)
                for description, amount in self.transactions:
                    self.transaction_listbox.insert(
                        tk.END, f"{description}: Rs. {amount}")
        except FileNotFoundError:
            self.transactions = []
        except json.JSONDecodeError:
            self.transactions = []

    # Function to calculate and update total income and expenses
    def calculate_total(self):
        income = sum(amount for _, amount in self.transactions if amount > 0)
        expenses = sum(amount for _, amount in self.transactions if amount < 0)
        self.total_income_label.config(text=f"Total Income: Rs. {income:.2f}")
        self.total_expenses_label.config(
            text=f"Total Expenses: Rs. {expenses:.2f}")

# Initialize and run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = FinanceTrackerApp(root)
    root.mainloop()
