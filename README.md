# Guess the word game

## Milestone project 3

This is a Guess the secret word game, wherein the player have a set amounts of tries to guess the secret word to win the game. 
The game generates a random secret word every round. 
The player chooses the difficulty level of the game; easy, normal or hard. Easy gives the player 10 tries to win, normal 7 tries and hard 5 tries. 
If the player guess the whole word correctly they win the game, if they run out of tries they loose and will have the option to start over.

## Live project app
[View live app here]()

## README table of content
- [Milestone project 3](#milestone-projekt-3)
- [Live project app](#live-project-app)
- [Screenshots of app](#screenshots-of-app)
- [Flowchart](#flowchart)
- [User stories](#user-stories)
- [Color scheme and imagery](#color-scheme-and-imagery)
- [Features](#features)
  -[]
  -[]
  -[]
- [Technology](#technology)
   - [Languages used](#languages-used)
   - [Other applications used](#other-applications-used)
- [Testing](#testing)
   - [Player Experience](#player-experience)
   - [Code testing](#code-testing)
   - [Known issues](#known-issues)
- [Deployment](#deployment)
    -[Github and git](#github-and-git)
    -[Heroku](#heroku)
- [Credits](#credits)
    - [Content](#content)
    - [Acknowledgement](#acknowledgement)
    - [External sources used](#external-sources-used)

## Screenshots of app

![](https://github.com/EmelieMarkkanen/p3-guess-the-word-game/blob/main/docs/images/Printscreen1.jpg)

### Guess the word game

#### Start game
![Game start](https://github.com/EmelieMarkkanen/p3-guess-the-word-game/blob/main/docs/images/Game1.jpg)

#### Choose difficulty level
![Choose a difficulty level](https://github.com/EmelieMarkkanen/p3-guess-the-word-game/blob/main/docs/images/Game2.jpg)

#### Guess a letter
![Guessing letters](https://github.com/EmelieMarkkanen/p3-guess-the-word-game/blob/main/docs/images/Game3.jpg)

#### Error messages
![Error messages](https://github.com/EmelieMarkkanen/p3-guess-the-word-game/blob/main/docs/images/Game4.jpg)

#### Win game
![Win game](https://github.com/EmelieMarkkanen/p3-guess-the-word-game/blob/main/docs/images/Game6%20-%20win.jpg)

#### Lose game
![Lose game](https://github.com/EmelieMarkkanen/p3-guess-the-word-game/blob/main/docs/images/Game5%20-%20lose.jpg)

## Flowchart
I created the flowchart for this project using Lucidchart.
<br>
[View PDF of flowchart here](https://github.com/EmelieMarkkanen/p3-guess-the-word-game/blob/main/docs/pdf/Guess-the-word-flowchart.pdf)

## User stories
-
-
-
-

## Color scheme and imagery
To add text color to the terminal I've used the imported library [Colorama](https://pypi.org/project/colorama/).
To create the ASCII Art on the game start screen I've used [ASCII Art Generator](https://patorjk.com/software/taag/#p=display&h=2&v=2&f=Big&t=Guess%20the%0Asecretword!)


## Features
-
-
-

## Technology

### Languages used
For this project I've used [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

### Other applications used
[Github](https://github.com/) and [Lucidchart](https://lucid.app/)

## Testing

### Player Experience

### Code testing
Git pod have pep8 installed for code checking. 
<br>
Testing have been done continuously during creation. 

### Known issues
One bug found by one user, but I've not been able to recreate the issue. The input line shows both player name and already guessed letters. 
![](/workspace/p3-guess-the-word-game/docs/images/bug.jpg)

## Deployment

### Github and git
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

### External sources used
- https://pypi.org/project/colorama/
- https://www.lucidchart.com/pages/
- https://www.reddit.com/r/learnpython/comments/l10k8h/is_there_a_way_to_unpack_a_list_with_f_stings/
- ASCII Art Generator https://patorjk.com/software/taag/#p=display&h=2&v=2&f=Big&t=Guess%20the%0Asecretword!
- https://www.w3schools.com/python/default.asp

Heroku https://p3-guess-the-word.herokuapp.com/


