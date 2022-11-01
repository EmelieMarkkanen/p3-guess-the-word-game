import random
import sys
from dictionary import dictionary

#Colorama module
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

def title_page():
    """Show title page for game
    """
    print(Fore.BLUE + """
   _____                       _   _                   
  / ____|                     | | | |                  
 | |  __ _   _  ___  ___ ___  | |_| |__   ___          
 | | |_ | | | |/ _ \/ __/ __| | __| '_ \ / _ \         
 | |__| | |_| |  __/\__ \__ \ | |_| | | |  __/         
  \_____|\__,_|\___||___/___/  \__|_| |_|\___|     _ _ 
                        | |                       | | |
  ___  ___  ___ _ __ ___| |___      _____  _ __ __| | |
 / __|/ _ \/ __| '__/ _ \ __\ \ /\ / / _ \| '__/ _` | |
 \__ \  __/ (__| | |  __/ |_ \ V  V / (_) | | | (_| |_|
 |___/\___|\___|_|  \___|\__| \_/\_/ \___/|_|  \__,_(_)
    """)

def select_difficulty():
    """
    Let player set the game difficulty level
    """
    print("Please select a difficulty level\n")
    print(Fore.GREEN + "Type 'E' for Easy")
    print(Fore.YELLOW + "Type 'N' for Normal")
    print(Fore.RED + "Type 'H' for Hard")

    difficulty = False
    while not difficulty:
        options = input().upper()
        if options == "E":
            difficulty = True
            tries = 10
            return tries
        elif options == "N":
            difficulty = True
            tries = 7
            return tries
        elif options == "H":
            difficulty = True
            tries = 5
            return tries
        else:
            print("Please select E, N or H to choose game difficulty level.")

def welcome_message():
    """
    Welcome the player and let them enter their name.
    """
    player_name = None
    while True:

        player_name = input("Please enter your name to play\n").capitalize() #Ask player to enter their name

        if not player_name.isalpha():
            print("Name must be letters only") #Player name can only be alphabetical letters
            continue
        else:
            print("\nWelcome to Guess the secret word, " + Fore.CYAN + f"{player_name}" + Fore.WHITE + "!\n") #Welcome player to the game
            break

def get_word():
    """
    Generates a random word from dictionary.py in capital letters
    """
    word = random.choice(dictionary)
    return word.upper()

def game():
    """
    Explain the rules of the game
    Player have X tries to guess the word - generated from select_difficulty()
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
    tries = select_difficulty()
    display = "_" * len(word)
    game_over = False
    guessed_letters = []
    print(Fore.CYAN + f"\nThe rules are simple; you have {tries} tries to guess the secret word.")
    print(Fore.CYAN + "Guess the wrong letter and go down one try. \nGuess all the letters of the word correctly to win!\n")

    while not game_over:
        print(f"You have " + str(tries) + " tries left.")
        print(f"You have guessed these letters: {' '.join(str(x) for x in guessed_letters)} \n")
        print(display)
        guess = input("Please guess a letter: ").upper() 

        if not guess.isalpha():
            print(Fore.YELLOW + "You can only guess alphabetical letters") #Player can only guess alphabetical letters
            continue
        if len(guess) > 1:
            print(Fore.YELLOW + "You can only guess one letter at a time") #Player can only guess one letter at a time
            continue
        if guess in guessed_letters:
            print(Fore.YELLOW + "You have already guessed that letter") #Player can only guess the same letter once
            continue
        
        #Check if letter is correct/incorrect, deduct tries if incorrect, add letter to guessed_letters, display if correct letter
        i = 0
        if guess in word: 
            while word.find(guess, i) != -1:
                i = word.find(guess, i)
                display = display[:i] + guess + display[i + 1:]
                i += 1
            print(Fore.BLUE + "You guessed a correct letter!") 
            guessed_letters.append(guess)
        else: 
            print(Fore.RED + f"Sorry, the letter {guess} is not in the word.") 
            tries -= 1
            guessed_letters.append(guess)

        if word == display:
            print(Fore.GREEN + f"\nGood job! You guessed the correct word! The word was {word}!\n") #Player guessed the right word and win the game
            game_over = True
        if tries == 0:
            print(Fore.RED + f"\nOh no! You are out of tries and lost the game. The word was {word}.\n") #Player ran out of tries and loose the game
            game_over = True
        
    play_again = input(Fore.YELLOW + "Would you like to play again? \nType 'Y' to play again, or type any other key to quit.\n").upper() #Ask player to restart or quit game

    if play_again == "Y":
        print(Fore.GREEN + "Let's play again, good luck!\n") #Restart game
        game()
    else: 
        print("Thank you for playing, good bye!") #Quit game
        sys.exit()
        
def main():
    """
    Call game functions
    """
    title_page()
    welcome_message()
    game()

main()