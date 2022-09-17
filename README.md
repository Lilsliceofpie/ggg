# Battleships
Battleships is a game in which each player receives a game board and five ships. The objective of the game is to guess the location of the other players ships and sink them before they sink your ships. This is a simplified version in which the player playes against the computer and only has a limited amount of guesses.

## Rules
The player and computer both start with 5 ships each, the player must input a row(1-5) and column(A-E) and try to destroy all of the computers ships. The player has 8 chances to guess, if they run out of chances or if the computer destroys all the players ships, its game over.

![](screenshots/Screenshot%20(47).png)

## Features

- __Random board generation__

  - Ships are randomly placed on both the player and computers boards.
  - The player cannot see the location of the computers ships.

- __Accepts user input__
- __Keeps track of turns taken__
- __Input validation and error checking__

  - Will not allow user to input a row or column outside of the grid.
  - The user must input a number for the row and a letter for the column selection. 
  - The user cannot input the same guess twice.
  
![](screenshots/Screenshot%20(48).png)

## Future features to implement

- __Allow player to select board size__
- __Allow player to place ships in location of their choice__
- __Have different sized ships__

## Testing
- I tested that the site works in different browsers: chrome, Internet explorer, DuckDuckGo.
- I put the code through PEP8 and confirmed that there are no errors
- I tested it in my local terminal and the code institute Heroku terminal

## Bugs
- Initially it would not accept lowercase letters as valid input from the user, i fixed this with the .upper() function.

## Validator testing
- PEP8: No errors were returned when passed through the validator.

![](screenshots/Screenshot%20(46).png)

## Deployment
- This project was deployed using Code institutes mock terminal for Heroku.

## Credits
- Some of the code in the make_ships(), player_input() and count_hits() functions was borrowed from this youtube video -https://youtu.be/tF1WRCrd_HQ
- Code Institute for the deployment terminal .