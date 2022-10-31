# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random
import sys
from dictionary import dictionary

def welcomeMessage():
    """
    Welcome player, explain the rules and let them enter their name.
    """
    player_name = None
    while True:

        player_name = input("Please enter your name\n").capitalize()

        if not player_name.isalpha():
            print("Name must be letters only")
            continue
        else:
            print(f"Welcome to Guess the word, {player_name}!\n")
            break
    
    print("The rules are simple; you have 6 tries and need to guess the secret word.")
    print("Guess the wrong letter and loose a try, guess all the letters of the whole word correctly to win!\n")

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

    while not game_over:
        print(f"You have " + str(tries) + " tries left")
        print(display)
        guess = input("Please guess a letter: ").upper()

        if not guess.isalpha():
            print("You can only guess alphabetical letters")
            continue
        if guess in display:
            print("You have already guessed that letter")
            continue
        if len(guess) > 1:
            print("You can only guess one letter at a time")
            continue

        i = 0
        if guess in word:
            while word.find(guess, i) != -1:
                i = word.find(guess, i)
                display = display[:i] + guess + display[i + 1:]
                i += 1
            print("You guessed one letter correctly!")
        else:
            print(f"Sorry, the letter {guess} was not in the word.")
            tries -= 1

        if word == display:
            print(f"You guessed the correct word! The word was {word}!\n")
            game_over = True
        if tries == 0:
            print(f"Sorry, you are out of tries and lost the game. The word was {word}.\n")
            game_over = True
        
    play_again = input("Would you like to play again? Type 'y' to play, type any other key to quit.\n")

    if play_again == "y":
        print("Let's play again, good luck!\n")
        welcomeMessage()
        game()
    else: 
        print("Thank you for playing, good bye!")
        sys.exit(0)

def main():
    """
    Call game functions
    """
    welcomeMessage()
    game()

main()