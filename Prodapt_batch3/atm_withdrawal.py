balance = 5000
amount=int(input("enter withdrawal amount:"))

if amount <= balance and amount % 100 == 0:
    balance -= amount
    print("withdrawal successful")
    print("remaining balance:", balance)
else:
    print("invalid withdrawal amount")
    