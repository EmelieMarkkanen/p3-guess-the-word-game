# Guess the word game

## Milestone project 3

This is a Guess the secret word game, wherein the player have a set amount of tries to guess the secret word to win the game. 
The game generates a random secret word every round. 
The player chooses the difficulty level of the game; easy, normal or hard. Easy gives the player 10 tries to win, normal 7 tries and hard 5 tries. 
If the player guess the whole word correctly they win the game, if they run out of tries they loose and will have the option to start over.

![](https://github.com/EmelieMarkkanen/p3-guess-the-word-game/blob/main/docs/images/Printscreen1.jpg)
Screenshot created using [Am I Responsive](https://ui.dev/amiresponsive)

## Live project app
[View live app here](https://p3-guess-the-word.herokuapp.com/)

## README table of content
- [Milestone project 3](#milestone-projekt-3)
- [Live project app](#live-project-app)
- [User stories](#user-stories)
- [Flowchart](#flowchart)
- [Color scheme and imagery](#color-scheme-and-imagery)
- [Features](#features)
- [Future features to add ](#future-features-to-add)
- [Technology](#technology)
    - [Languages used](#languages-used)
    - [Other applications used](#other-applications-used)
- [Testing](#testing)
    - [Player Experience](#player-experience)
    - [Code testing](#code-testing)
- [Deployment](#deployment)
    - [Gitpod and git](#github-and-git)
    - [Heroku](#heroku)
- [Credits](#credits)
    - [Content](#content)
    - [Acknowledgement](#acknowledgement)
    - [External sources used](#external-sources-used)


## User stories
- Aa a potential user I should easily understand what kind of application this is
- As a potential user I would like to get clear and logical feedback to my choices during the game
- As a potential user I would like to be able to choose different levels of difficulty for the game
- As a potential user I would like to be able to track my progress of the game and see weather I win or loose

## Flowchart
I created the flowchart for this project using Lucidchart.
<br>
[View PDF of flowchart here](https://github.com/EmelieMarkkanen/p3-guess-the-word-game/blob/main/docs/pdf/Guess-the-word-flowchart.pdf)

## Color scheme and imagery
To add text color to the terminal I've used the imported library [Colorama](https://pypi.org/project/colorama/).
To create the ASCII Art on the game start screen I've used [ASCII Art Generator](https://patorjk.com/software/taag/#p=display&h=2&v=2&f=Big&t=Guess%20the%0Asecretword!).

## Features
- Player can enter their name
- Choice of difficulty, amount of tries changes accordingly (10, 7 or 5 tries)
- Random word generator
- Encrypted word
- Guessed letters are displayed 
- Validation for non alphabetical characters, duplicate entries or multiple character entries
- Tries not deducted if duplicate, non alphabetical or multiple characters entered
- Messages in different colors to highlight information and replies to player
- Choice to restart or quit game after win/lose

## Future features to add 
- Add better visual aspects to make the app more interesting for the user
- Create different word categories for the user to choose between
- Add a hint function with a set amount of hints to use every round

## Technology

### Languages used
For this project I've used [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

### Other applications used
[Github](https://github.com/) and [Lucidchart](https://lucid.app/)

## Testing

### Player Experience
- Aa a potential user I should easily understand what kind of application this is
    - The starting visuals show the name of the game
![Game start](https://github.com/EmelieMarkkanen/p3-guess-the-word-game/blob/main/docs/images/Game1.jpg)

- As a potential user I would like to be able to choose different levels of difficulty for the game
![Choose a difficulty level](https://github.com/EmelieMarkkanen/p3-guess-the-word-game/blob/main/docs/images/Game2.jpg)

- As a potential user I would like to get clear and logical feedback to my choices during the game
    - Instructions to enter player name, choose a difficulty level and game rules are easy to follow
    - The player gets instant feedback in different colors depending on choice, and feedback with error messages if incorrect choices are made
![Error messages](https://github.com/EmelieMarkkanen/p3-guess-the-word-game/blob/main/docs/images/Game4.jpg)

- As a potential user I would like to be able to track my progress of the game and see weather I win or loose
    - Guessed letters are tracked and shown. Correct letters are added to the word, all letters are added to the list of guessed letters.
    - Win or lose message is shown after the player guess the right word or run out of tries
![Guessing letters](https://github.com/EmelieMarkkanen/p3-guess-the-word-game/blob/main/docs/images/Game3.jpg)
![Win game](https://github.com/EmelieMarkkanen/p3-guess-the-word-game/blob/main/docs/images/Game6%20-%20win.jpg)
![Lose game](https://github.com/EmelieMarkkanen/p3-guess-the-word-game/blob/main/docs/images/Game5%20-%20lose.jpg)


### Code testing
Gitpod have PEP8 installed for code validation. PEP8 errors will be underlined in red, as well as being listed in the 'Problems' tab beside the terminal.
In Gitpod I've also run pylint run.py to check for any error messages and resolve those. 
<br>
Testing have been done continuously during creation in Gitpod terminal and Code Institute Heroku terminal.

## Deployment

### Gitpod and git
1. I created a repository in Github, named it p3-guess-the-word-game, and used the template Code-Institute-org/python-essentials-template
2. Once the repository is created, click the green button to the right (Gitpod) to open Gitpod
3. In the terminal I've used the run.py file provided by the template
4. I created a docs folder to hold PDF:s and images
5. Once folders and files are created I used Git commands to add the changes in the files to the staging area and push the changes to my repository

### Heroku
This project was deployed using Code Institutes mock terminal for Heroku.

1. Log in to Heroku and click "New" and "Create new app"
2. Name the new app and click "Create new app".
3. In "Settings" select "BuildPack" and select Python and Node.js. (Python must be at the top of the list).
4. While still in "Settings", click "Reveal Config Vars" and add the following; KEY: PORT, VALUE: 8000.
5. Click on "Deploy" and select your deploy method and search for repository name.
6. Click "Connect" on selected repository.
7. Either choose "Enable Automatic Deploys" or "Deploy Branch" in the manual deploy section.
8. Heroku will now deploy the app.

## Credits

### Content
I've used this [tutorial](https://www.youtube.com/watch?v=WpHieqiOVFE&list=PLQGawZx_TVhrNvQBAKPrPaMxZmw2RYTa1&index=15) to build a portion of this game, created by John Seiffert. Some similarities will occur. 
<br>
Design and other content written by me. 

### Acknowledgement

#### Thank you to <br>
Code institute for the mock terminal<br>
Jan-Åke Fonnaland and Anders Colliander for testing<br>
CI Peer review on slack <br>
My mentor Rohit for valuable input and feedback

### External sources used
- https://pypi.org/project/colorama/
- https://www.lucidchart.com/pages/
- https://www.reddit.com/r/learnpython/comments/l10k8h/is_there_a_way_to_unpack_a_list_with_f_stings/
- https://patorjk.com/software/taag/#p=display&h=2&v=2&f=Big&t=Guess%20the%0Asecretword!
- https://www.w3schools.com/python/default.asp


