sequenceNumber = int(input("Enter sequence number to be printed: "))

firstNum = 0
secondNum = 1

for number in range(1, sequenceNumber):
    temp = secondNum
    secondNum = firstNum + secondNum
    firstNum = temp
print(temp)
