def get_income():
    return float(input("Enter your monthly income: "))

def get_expenses():
    categories = {}
    while True:
        try:
            category = input("Enter expense category (or 'done' to finish): ")
            if category.lower() == 'done':
                break
            amount = float(input(f"Enter amount for {category}: "))
            if category in categories:
                categories[category] += amount
            else:
                categories[category] = amount
        except ValueError:
            print("Please enter a valid number.")
    return categories

def calculate_savings(income, expenses):
    total_expenses = sum(expenses.values())
    return income - total_expenses

def main():
    income = get_income()
    expenses = get_expenses()
    savings = calculate_savings(income, expenses)
    print(f"Your monthly savings are: ₹{savings:.2f}")

if __name__ == "__main__":
    main()
