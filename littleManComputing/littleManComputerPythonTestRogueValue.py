rogueValue = 0
total = 0

while rogueValue != 99:
    rogueValue = int(input("Enter a number: "))
    if rogueValue != 99:
        total += rogueValue

print("total: ", total)
