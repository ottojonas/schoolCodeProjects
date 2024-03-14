numberOne = int(input("Enter first number: "))
numberTwo = int(input("Enter second number: "))
numberThree = int(input("Enter third number: "))

if numberOne > numberTwo:
    numberOne, numberTwo = numberTwo, numberOne

if numberOne > numberThree:
    numberOne, numberThree = numberThree, numberOne

if numberTwo > numberThree:
    numberTwo, numberThree = numberThree, numberTwo

print(f"Numbers in order: {numberOne}, {numberTwo}, {numberThree}")
