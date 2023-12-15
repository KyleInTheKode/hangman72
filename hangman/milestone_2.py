import random
import os

def get_word():
    word_list = ["mango","strawberry","cherry","passion","apple"]
    return random.choice(word_list).lower()

def get_input():
    word = get_word()
    guessed_letters = []
    print(word)
    while True:
        print(f"Guessed Letters: {guessed_letters}")
        guess = input("Please enter a letter: ").lower()
        os.system("cls")
        if len(guess) == 1:
            if guess in word:
                if guess in guessed_letters:
                    print("You have already guessed this letter!")
                else:
                    print("Good Guess!")
                    guessed_letters.append(guess)
            else:
                print("Incorrect Guess!")
            print(f"You have guessed: {guess}")
        else:
            print("Incorrect Guess!")

get_input()