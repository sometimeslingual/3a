from functools import reduce

def get_expenses():
    expenses = []
    num_expenses = int(input("How many expenses do you have? "))
    for i in range(num_expenses):
        expense_type = input(f"Enter the type of expense {i+1}: ")
        expense_amount = float(input(f"Enter the amount for {expense_type}: "))
        expenses.append((expense_type, expense_amount))
    return expenses

def analyze_expenses(expenses):
    total_expense = reduce(lambda x, y: x + y[1], expenses, 0)
    highest_expense = max(expenses, key=lambda x: x[1])
    lowest_expense = min(expenses, key=lambda x: x[1])

    return total_expense, highest_expense, lowest_expense

def main():
    expenses = get_expenses()
    total, highest, lowest = analyze_expenses(expenses)

    print(f"\nTotal expenses: ${total:.2f}")
    print(f"Highest expense: {highest[0]} - ${highest[1]:.2f}")
    print(f"Lowest expense: {lowest[0]} - ${lowest[1]:.2f}")

if __name__ == "__main__":
    main()
