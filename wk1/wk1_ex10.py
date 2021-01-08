from math import pow, log10

print("Good day,")
a = int(input("please enter a: "))
b = int(input("please enter b: "))

print(f"sum of a and b is {a+b}.")
print(f'diff when b is subtracted from a is {a-b}.')
print(f'product of a and b is {a*b}.')
print(f'quotient when a is dived by b is {a/b}.')
print(f'remainder when a is divided by b is {a%b}.')
print(f'log10(a) is {log10(a)}.')
print(f'a^b is {pow(a,b)}.')
