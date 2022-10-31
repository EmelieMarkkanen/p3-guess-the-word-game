# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random
from dictionary import dictionary

word = "cat"
#word = random.choice(dictionary)

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
    
    print("The rules are simple; you have 6 tries and need to guess the secret word.")
    print("Guess the wrong letter and loose a try, guess all the letters of the whole word correctly to win!\n")

#def get_word():
    """
    Generates a random word from dictionary.py in capital letters
    return word.upper() 
    """

def game():
    tries = 6
    display = "_" * len(word)
    game_over = False

    while not game_over:
        print(f"You have " + str(tries) + " tries left")
        print(display)
        guess = input("Please guess a letter: ")

        i = 0
        if guess in word:
            while word.find(guess, i) != -1:
                i = word.find(guess, i)
                display = display[:i] + guess + display[i + 1:]
                i += 1
            print("You guessed correctly!")
        else:
            print("Sorry, that letter was not in the word :(")
            tries -= 1

        if word == display:
            print(f"You guessed the correct word! The word was {word}!")
            game_over = True
            print("Would you like to play again? Type 'yes' to play, type 'no' to quit.")
        if tries == 0:
            print(f"Sorry, you are out of tries and loose the game. The word was {word}.")
            game_over = True
            print("Would you like to play again? Type 'yes' to play, type 'no' to quit.")
        

def main():
    """
    Call game functions
    """
    welcomeMessage()
    game()

main()