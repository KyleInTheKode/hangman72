import random
import os
from hangman_picture import hangman_pic

word = ""
guessed_letters = []
incorrect_letters = []


def get_word():
    global word
    word_list = ["mango","strawberry","cherry","passion","apple"]
    word = random.choice(word_list)

def get_input():
    os.system("cls")
    #print(f"Testing. The chosen word is: {word.capitalize()}")
    while True:
        print(hangman_pic[len(incorrect_letters)])
        game_test()
        print(f"Guessed Letters: {guessed_letters}")
        print(f"Incorrect Letters: {incorrect_letters}")
        if game_status() == True:
            break
        guess = input("\nPlease enter a letter: ").lower()
        os.system("cls")
        check_letter(guess)

def game_status():
    if len(incorrect_letters) >= len(hangman_pic) -1:
        #os.system("cls")
        print(f"\nYou have lost! The answer was: {word.upper()}")
        return True
    if set(word) == set(guessed_letters):
        #os.system("cls")
        print(f"\nYou have won!")
        return True


def check_letter(guess):
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


def game_test():
    for letter in word:
        if letter in guessed_letters:
          print(f"{letter.upper()} ",end="")
        else:
            print("_ ",end="")
    print("\n")

def start_game():
    get_word()
    get_input()

    

start_game()