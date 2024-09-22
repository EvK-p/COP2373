# Import the reduce function from the functools module
from functools import reduce

# Define list of expenses
expenses = []

# Creates function to calculate total amount
def calculate_expenses(expenses):
    return reduce(lambda x, y: x + y[1], expenses, 0)

# Creates function to calculate the highest expense
def highest_amount(expenses):
    return reduce(lambda x, y: x if x[1] > y[1] else y, expenses)

# Creates function to calculate the lowest expense
def amount_lowest(expenses):
    return reduce(lambda x, y: x if x[1] < y[1] else y, expenses)

# Asking user for their monthly expenses
while True:
    type_of_expense = input("\nPlease enter your expense (or 'done' to run the calculator): ")
    if type_of_expense.lower() == 'done':
        print('\n Processing...')
        break
    try: # Asks the user how much they pay for the previously entered expense
        amount = float(input(f"Enter the amount you pay for {type_of_expense} each month: $ "))
        expenses.append((type_of_expense, amount))
    except ValueError: # If they type an incorrect character, this message will display
        print("INVALID INPUT. Please type a valid number.\n")

# If there are any expenses, process them
if expenses:
    total_expense = calculate_expenses(expenses)
    highest_expense = highest_amount(expenses)
    lowest_expense = amount_lowest(expenses)

# Display the total, highest, and lowest amounts to the user
    print("\n DONE")
    print("\nThis is how much you pay every month: ${:,.2f}".format(total_expense))
    print(f"\nYou pay the most for: $ {highest_expense[0]} - ${highest_expense[1]:,.2f}")
    print(f"\nYou pay the least for: $ {lowest_expense[0]} - ${lowest_expense[1]:,.2f}")
