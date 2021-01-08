print("Good day,")
meal = float(input("please enter the cost of your meal: "))
tax = (7/100)*meal
tip = (18/100)*meal
print('your tax is $%.2f and tip amount is $%.2f and the grand total is $%.2f' % (tax, tip, tax+tip+meal))
