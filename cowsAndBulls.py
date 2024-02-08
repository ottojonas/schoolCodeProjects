import random

secretCode = [str(index) for index in random.sample(range(1, 9), 4)]
guesses = 0
while guesses < 100:
    userGuess = input("Enter a guess: ")
    if len(userGuess) != 4 or not userGuess.isdigit():
        print("Invalid guess, please enter a 4-digit number.")
        continue
    bulls = 0
    cows = 0
    for index in range(4):
        if userGuess[index] in secretCode:
            if userGuess[index] == secretCode[index]:
                bulls += 1
            else:
                cows += 1
    print(f"Bulls: {bulls}, Cows: {cows}")
    if bulls == 4:
        print("Congratulations! You guessed the code in {guesses} guesses.")
        break
    guesses += 1

if guesses == 100:
    print(f"You did not get the code, the code was: {secretCode}")
