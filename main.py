name = input("please type your name: ")
balance = input("what is your savings account balance: ")

rate = input("what is your monthly interest rate (rate must be 1.0 or under): ")

income = float(balance) * float(rate)
print("Hello " + name)

if float(rate) > 0:
    total = float(balance) + float(income)
    print("your income in interest monthly in dollars is: " + str(income) )
    print("this makes your new savings account balance: " + str(total))

else:
    print("you Have generated no money this month!")
    print("this means you savings account balance stays the same!")