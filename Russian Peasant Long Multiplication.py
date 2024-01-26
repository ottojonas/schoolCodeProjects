# Russian Peasant Long Multiplication
ans = 0 
op1 = int(input("Enter op1: "))
op2 = int(input("Enter op2: "))

while op1 > 0:
    if op1 % 2 != 0:
        ans += op2
        print(ans)
    
    op1 = op1 // 2
    op2 = op2 * 2
    print(op1, op2)

print("The answer is: ", ans)