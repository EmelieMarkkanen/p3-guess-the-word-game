# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random
from dictionary import dictionary

def welcomeMessage():
    """
    Welcome player, explain the rules and let them enter their name.
    """
    player_name = None
    while True:

        player_name = input("Please enter your name\n")

        if not player_name.isalpha():
            print("Name must be letters only")
            continue
        else:
            print(f"Welcome to Guess the word, {player_name}!\n")
            break
    
    print("The rules are simple; you have 6 lives and need to guess the secret word.")
    print("Guess the wrong letter and loose a life, guess all the letters of the whole word correctly to win!\n")

def get_word():
    """
    Generates a random word from dictionary.py in capital letters
    """
    word = random.choice(dictionary)
    return word.upper() 


def main():
    """
    Call functions in game
    """
    welcomeMessage()
    get_word()
    game()
    
main()