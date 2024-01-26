class Stack:
    def __init__(self, size):
        self.maxSize = size
        self.myStack = [None] * size
        self.createStack = ()
        self.topOfStack = -1

    def push(self, data):
        if self.isFull():
            print("Stack overflow")
        else:
            self.myStack[self.topOfStack] = data
            self.topOfStack += 1

    def isFull(self):
        returnValue = False
        if self.topOfStack == self.maxSize - 1:
            returnValue = True
        return returnValue

    def pop(self):
        if self.isEmpty():
            print("Stack underflow")
            return None
        else:
            self.topOfStack -= 1
            return self.myStack.pop()

    def isEmpty(self):
        return self.topOfStack == -1


class Calculator:
    def __init__(self):
        self.stack = Stack(5)

    def calculate(self, expression):
        tokens = expression.split()

        for token in tokens:
            if token.isdigit():
                self.stack.push(int(token))
            else:
                if self.stack.isEmpty():
                    print("Not enough operands")
                operand2 = self.stack.pop()
                operand1 = self.stack.pop()

                if token == "+":
                    result = operand1 + operand2
                elif token == "-":
                    result = operand1 - operand2
                elif token == "*":
                    result = operand1 * operand2
                elif token == "/":
                    result = operand1 / operand2
                self.stack.push(result)
        return self.stack.pop()


if __name__ == "__main__":
    calculator = Calculator()
    result = calculator.calculate("5 4 2 + *")
    print(result)
