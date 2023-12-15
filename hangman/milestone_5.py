import random
import os
from hangman_picture import hangman_pic

class HangMan:

    def __init__(self):
        self.word = ""
        self.guessed_letters = []
        self.incorrect_letters = []

    def __get_word(self):
        global word
        word_list = ["mango","strawberry","cherry","passion","apple"]
        self.word = random.choice(word_list)

    def __check_letter(self, guess, word, guessed_letters, incorrect_letters):
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters or guess in incorrect_letters:
                print("You have already guessed this letter!")
            else:
                if guess in word:
                    #Add to correct letters
                    guessed_letters.append(guess)
                else:
                    #Add to incorrect letters
                    incorrect_letters.append(guess)
        else:
            print("Invalid guess!")
            
    def __get_input(self):
        os.system('cls||clear')
        while True:
            print(hangman_pic[len(self.incorrect_letters)])
            self.__game_test(self.word, self.guessed_letters)
            print(f"Guessed Letters: {self.guessed_letters}")
            print(f"Incorrect Letters: {self.incorrect_letters}")
            if self.__game_status(self.word, self.guessed_letters, self.incorrect_letters) == True:
                break
            self.guess = input("\nPlease enter a letter: ").lower()
            os.system('cls||clear')
            self.__check_letter(self.guess, self.word, self.guessed_letters, self.incorrect_letters)

    def __game_status(self, word, guessed_letters, incorrect_letters):
        if len(incorrect_letters) >= len(hangman_pic) -1:
            print(f"\nYou have lost! The answer was: {word.upper()}")
            return True
        if set(word) == set(guessed_letters):
            print(f"\nYou have won!")
            return True

    def __game_test(self, word, guessed_letters):
        for letter in word:
            if letter in guessed_letters:
                print(f"{letter.upper()} ",end="")
            else:
                print("_ ",end="")
        print("\n")

    def start_game(self):
        self.__get_word()
        self.__get_input()

HangMan().start_game()