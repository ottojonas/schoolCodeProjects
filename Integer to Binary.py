number = int(input("Number input: "))
binary = []

while number != 0: 
    binary = [number % 2] + binary
    number = number // 2 
    print(binary)