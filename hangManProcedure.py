import random


def getWord(wordList):
    return random.choice(wordList)


def gameState(word, guessedLetters):
    displayedWord = "".join(
        [letter if letter in guessedLetters else "_" for letter in word]
    )
    print(f"word {displayedWord}")
    print(f"Guessed letters {" ".join(guessedLetters)}")


def getGuess(guessedLetters):
    while True:
        guess = input("Enter letter: ")
        if guess not in guessedLetters:
            return guess
        else:
            print("You have already used that letter")


def updateGame(word, guessedLetters, guess):
    isCorrectGuess = False
    if guess in word:
        if guess not in guessedLetters:
            guessedLetters.append(guess)
        isCorrectGuess = True
    elif guess not in word and guess in guessedLetters:
        print("You have already used that letter")
    else:
        if guess not in guessedLetters:
            guessedLetters.append(guess)
    return guessedLetters, isCorrectGuess


def isGameOver(word, guessedLetters, livesLeft):
    if livesLeft == 0 or set(word) == set(guessedLetters):
        return True
    return False


def main():
    wordList = ["iguana", "chameleon", "salamandar", "komodo", "gecko", "lounge"]
    word = getWord(wordList)
    guessedLetters = []
    maxAttempts = 10
    livesLeft = maxAttempts

    while not isGameOver(word, guessedLetters, livesLeft):
        gameState(word, guessedLetters)
        guess = getGuess(guessedLetters)
        guessedLetters, isCorrectGuess = updateGame(word, guessedLetters, guess)
        if not isCorrectGuess:
            livesLeft -= 1
            print(f"You lost a life, you have {livesLeft} lives left")
    if set(word) == set(guessedLetters):
        print("You win")
    else:
        print("You lose")


main()
