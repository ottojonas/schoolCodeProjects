import random

code = [random.randint(0, 9), random.randint(0, 9)]
for _ in range(10):
    guess = list(map(int, input("Enter a 2 digit code: ")))
    print(f"{sum(g == c for g, c in zip(guess, code))} digits in the correct place")
    if guess == code:
        print(f"Success you guessed the code: {code}")
        quit
    print("You did not guess the code")
print(f"The correct code is: {code}")
