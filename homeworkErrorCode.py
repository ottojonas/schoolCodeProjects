errorDigit = []
errorCode = []

#getting error digits from user 
errorDigit = [int(input(f"enter the error digits to be checked: ")) for _ in range(int(input(f"enter number of error digits to be checked: ")))]
print("the error digits being checked are: ", *errorDigit, sep = " ")

#getting error codes from user 
errorCode = [int(input(f"enter the error codes to be checked: ")) for _ in range(int(input(f"enter the number of error codes to be checked: ")))]
print("the error codes to be checked are: ", *errorCode, sep = "\n")

#defined function to find the first digit of the error codes
def findFirstDigit(errorCode): 
    if errorCode < 10: 
        return errorCode 
    return findFirstDigit(errorCode // 10)

#create a list of the first digits of error codes 
errorCodeFirst = [findFirstDigit(code) for code in errorCode]
errorCodesCheck = []
for i in range(len(errorCode)): 
    errorCodesCheck.append(errorCodeFirst[i])

#a defined function to find error codes which the error digits match and counting them 
def findErrorCodes(errorDigit, errorCodes): 
    total = 0 
    for i in range(len(errorDigit)): 
        for j in range(len(errorCodes)): 
            if errorDigit[i] == errorCodes[j] % 10: 
                total += 1 
    return total 

#outputs the total number of error codes which match the error digits 
total = findErrorCodes(errorDigit, errorCodeFirst)
print(f"there were a total of {total} error codes")