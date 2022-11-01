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

        player_name = input("Please enter your name to play\n").capitalize() #Ask player to enter their name

        if not player_name.isalpha():
            print("Name must be letters only") #Player name can only be alphabetical letters
            continue
        else:
            print("Welcome to Guess the word, " + Fore.MAGENTA + f"{player_name}" + Fore.WHITE + "!\n") #Welcome player to the game
            break
    
    print("The rules are simple; you have 6 tries to guess the secret word.")
    print("Guess the wrong letter and go down one try, guess all the letters of the word correctly to win!\n")

def get_word():
    """
    Generates a random word from dictionary.py in capital letters
    """
    word = random.choice(dictionary)
    return word.upper()

def game():
    """
    Player have 6 tries to guess the word
    Generates random word from dictionary.py and counts amount of letters in word
    Player have to guess only alphabetical letters
    Player can only guess the same letter once
    Player can only guess one letter at a time
    Letters guessed will be shown if correct/incorrect
    Letters guessed will be shown and updated after every guess
    Incorrect guess will deduct a try
    Correct letters will be shown in word
    The loop will end after the player guess the word or reached 0 tries
    After win/lose option to play again will be asked
    """
    word = get_word() 
    tries = 6
    display = "_" * len(word)
    game_over = False
    guessed_letters = []

    while not game_over:
        print(f"You have " + str(tries) + " tries left") #Show amount of tries left
        print(f"You have used these letters: {' '.join(str(x) for x in guessed_letters)}") #Show guessed letters
        print(display)
        guess = input("Please guess a letter: ").upper() #Ask player to guess a letter

        if not guess.isalpha():
            print(Fore.YELLOW + "You can only guess alphabetical letters") #Player can only guess alphabetical letters
            continue
        if len(guess) > 1:
            print(Fore.YELLOW + "You can only guess one letter at a time") #Player can only guess one letter at a time
            continue
        if guess in guessed_letters:
            print(Fore.YELLOW + "You have already guessed that letter") #Player can only guess the same letter once
            continue
        
        #Check if guessed letter is in the word
        i = 0
        if guess in word: 
            while word.find(guess, i) != -1:
                i = word.find(guess, i)
                display = display[:i] + guess + display[i + 1:]
                i += 1
            print(Fore.BLUE + "You guessed a correct letter!") #Player guessed correct letter
            guessed_letters.append(guess)
        else:
            print(Fore.RED + f"Sorry, the letter {guess} is not in the word.") #Player guessed wrong letter
            tries -= 1
            guessed_letters.append(guess)

        if word == display:
            print(Fore.GREEN + f"You guessed the correct word! The word was {word}!\n") #Player guessed the right word and win the game
            game_over = True
        if tries == 0:
            print(Fore.RED + f"Sorry, you are out of tries and lost the game. The word was {word}.\n") #Player ran out of tries and loose the game
            game_over = True
        
    play_again = input(Fore.YELLOW + "Would you like to play again? Type 'y' to play again, type any other key to quit.\n") #Ask player to restart or quit game

    if play_again == "y":
        print("Let's play again, good luck!\n") #Restart game
        welcome_message()
        game()
    else: 
        print("Thank you for playing, good bye!") #Quit game
        sys.exit(0)

def main():
    """
    Call game functions
    """
    welcome_message()
    game()

main()