print("Good day,")
interest = 4
principle = int(input("Enter amount deposited: "))
for i in range(1, 4):
    interest_per_year = ((interest/100)*principle)+principle
    print(f'Year {i}: Amount in account is $%.2f' % interest_per_year)
    principle = interest_per_year
