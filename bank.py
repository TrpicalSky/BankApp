customer_name = input("Welcome, what is your name: ")
starting_balance = 5000.25

def welcomeCustomer(name,balance):
    print(f"Hello {name} your starting balance is ${starting_balance}")
welcomeCustomer(customer_name,starting_balance)

paycheck = float(input("How much of your paycheck would you like to deposit? "))
starting_balance = starting_balance + paycheck

expenditure_item = input("You bought something what was it.")
expenditure = float(input(f"How much did the {expenditure_item} cost? "))

def checking_balance(user_name, balance, expense_item, expense_amount):
    ending_balance = balance - expenditure
    print(f"Your ending balance is {ending_balance} after all things considered")

checking_balance(customer_name,starting_balance, expenditure_item, expenditure)