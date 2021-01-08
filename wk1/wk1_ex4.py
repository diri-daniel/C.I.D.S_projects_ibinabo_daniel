print("Good day,")
width = float(input("please enter the width of the field (in feet): "))
length = float(input("please enter the length of the field (in feet): "))
area = width*length
acres = area/43560
print(f'the area of the field is %.2ffeet' % acres)
