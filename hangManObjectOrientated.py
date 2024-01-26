import random


class Word:
    def __init__(self, word):
        self.word = word
        self.revealed = ["_"] * len(word)

    def checkLetter(self, letter):
        return letter in self.word

    def revealLetter(self, letter):
        for i in range(len(self.word)):
            if self.word[i] == letter:
                self.revealed[i] = letter

    def isFullyRevealed(self):
        return "_" not in self.revealed


class Player:
    def __init__(self):
        self.incorrectGuesses = []
        self.lives = 6
        self.unusedLetters = set("abcdefghijklmnopqrstuvwxyz")

    def guess(self, letter):
        self.unusedLetters.remove(letter)
        return letter

    def addIncorrectGuess(self, guess):
        self.incorrectGuesses.append(guess)
        self.lives -= 1
        if guess in self.unusedLetters:
            self.unusedLetters.remove(guess)


class Hangman:
    def __init__(self, word, player):
        self.word = Word(random.choice(words))
        self.player = player

    def startGame(self):
        while not self.word.isFullyRevealed() and self.player.lives > 0:
            guess = input("Enter a letter: ")
            if guess not in self.player.unusedLetters:
                print("You have already used that letter, try again")
                continue
            guess = self.player.guess(guess)
            if self.word.checkLetter(guess):
                self.word.revealLetter(guess)
            else:
                self.player.addIncorrectGuess(guess)
            print("".join(self.word.revealed))
            print(f"Unused letters: {" ".join(sorted(self.player.unusedLetters))}")
            print(f"Incorrect guesses: {self.player.incorrectGuesses}")
            print(f"You lost a life. Lives remaining: {self.player.lives}")

        if self.word.isFullyRevealed():
            print("You win")
        else:
            print("you lose")


words = ["iguana", "chameleon", "salamandar", "komodo", "gecko", "lounge"]
player = Player()
game = Hangman("hangman", player)
game.startGame()
