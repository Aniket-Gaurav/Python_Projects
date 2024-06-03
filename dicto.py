categories = {}
while True:
    try:
        category = input("Enter expense category or 'done' to finish: ")
        if category.lower() == 'done':
            break
        amount = float(input(f"Enter amount for {category}: "))
        if category in categories:
            categories[category] += amount
        else:
            categories[category] = amount
    except ValueError:
        print("Please enter a valid number.")

print("Expense breakdown:")
for category, amount in categories.items():
    print(f"{category}: ₹{amount:.2f}")