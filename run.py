# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random
import sys
from dictionary import dictionary

#Colorama module
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)


def welcome_message():
    """
    Welcome the player, explain the rules and let them enter their name.
    """
    player_name = None
    while True:

        player_name = input("Please enter your name to play\n").capitalize()

        if not player_name.isalpha():
            print("Name must be letters only")
            continue
        else:
            print("Welcome to Guess the word, " + Fore.MAGENTA + f"{player_name}" + Fore.WHITE + "!\n")
            break
    
    print("The rules are simple; you have 6 tries to guess the secret word.")
    print("Guess the wrong letter and go down one try, guess all the letters of the whole word correctly to win!\n")

def get_word():
    """
    Generates a random word from dictionary.py in capital letters
    """
    word = random.choice(dictionary)
    return word.upper()

def game():
    word = get_word()
    tries = 6
    display = "_" * len(word)
    game_over = False
    guessed_letters = []

    while not game_over:
        print(f"You have " + str(tries) + " tries left")
        print(display)
        guess = input("Please guess a letter: ").upper()

        if not guess.isalpha():
            print(Fore.YELLOW + "You can only guess alphabetical letters")
            continue
        if len(guess) > 1:
            print(Fore.YELLOW + "You can only guess one letter at a time")
            continue
        if guess in guessed_letters:
            print(Fore.YELLOW + "You have already guessed that letter")
            continue

        i = 0
        if guess in word:
            while word.find(guess, i) != -1:
                i = word.find(guess, i)
                display = display[:i] + guess + display[i + 1:]
                i += 1
            print(Fore.BLUE + "You guessed a correct letter!")
            guessed_letters.append(guess)
        else:
            print(Fore.RED + f"Sorry, the letter {guess} was not in the word.")
            tries -= 1
            guessed_letters.append(guess)

        if word == display:
            print(Fore.GREEN + f"You guessed the correct word! The word was {word}!\n")
            game_over = True
        if tries == 0:
            print(Fore.RED + f"Sorry, you are out of tries and lost the game. The word was {word}.\n")
            game_over = True
        
    play_again = input(Fore.YELLOW + "Would you like to play again? Type 'y' to play again, type any other key to quit.\n")

    if play_again == "y":
        print("Let's play again, good luck!\n")
        welcome_message()
        game()
    else: 
        print("Thank you for playing, good bye!")
        sys.exit(0)

def main():
    """
    Call game functions
    """
    welcome_message()
    game()

main()