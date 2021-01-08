print("Good day,")
US_EFF = float(input("please enter the fuel efficiency in MPG: "))
CAD_EFF = 62.13727/(0.26417*US_EFF)
print(f'Fuel efficiency is {CAD_EFF} l/100km')
