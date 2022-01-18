import random

class Hangman:
    def __init__(self):
        self.word = random.choice(open("/usr/share/dict/words").read().splitlines())
        self.guesses = set()
        self.lives = 10

    def play(self):
        while True:
            word_guessed = self.word
            for i in range(0, len(word_guessed)):
                if (word_guessed[i] not in self.guesses):
                    word_guessed = word_guessed.replace(word_guessed[i], '_')
            print("{}".format(word_guessed))
            if self.guesses is not set():
                print("Guessed so far: {}".format(' '.join(self.guesses)))
            letter = input("You have {} lives. Guess a letter: ".format(self.lives))
            if letter in self.guesses:
                print("You already guessed {}".format(letter))
            else:
                if letter not in self.word:
                    self.lives = self.lives - 1
                self.guesses.add(letter)
            if (0 not in [c in self.guesses for c in self.word]) == True:
                print("You won! The word was {}".format(self.word))
                break
            if self.lives == 0:
                print("You lost! The word was {}".format(self.word))
                break

if __name__ == '__main__':
    hangman = Hangman()
    hangman.play()