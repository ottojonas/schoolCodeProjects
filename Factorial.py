def factorial(factNum):
    if factNum == 1: 
        return 1     
    else: 
        factNum = factNum * factorial(factNum - 1) 
    return factNum 

num = int(input("Enter number: "))    
print(factorial(num))