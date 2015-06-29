# python_battle_game

**a game made on an airplane.**

This game isn't, but hopefully will become a turn based RPG. There's no story right now, just pure battling. All that you can do at this point is attack your enemy who attacks you automatically back. At this point there is no difficulty and you will win every round (use the fireball).

## Project Files

### main.py

*You would run the game from here. Runs the init_game method from the game class and also provides the ability to play the game again.*

### game.py

*This is where the magic happens. game.py contains init_game() which is where the main game loop resides. We do most of our input handling in this method as well as our attack phases.*


### person.py

*This is our person object. We use it to initialize our player and enemy for version 1 of this game.*

- **health**
- **MAX_HEALTH**
- **p_type**
- **defense**
- **attack() returns a damage value**
- **isCrit() returns true/false based on if attack crits**
- **isDead() returns true/false based on if person has less than 0**
- *speed (Unimplemented)*

### util.py

*This file includes all of our utility functions that are used several times across most classes.*

- **is_valid_input()** -> uses regex to determine if the input is valid
- **printTitle()** -> takes a string and returns a nicely formatted title
- **render_health_bar()** -> Rounds a percentage and returns an ascii health bar

## Features to Implement

- **I want to turn this into a pokemon clone. That said I should do the following things**
  - Create a monster class for each creature
  - Add the ability to switch between creatures (3 allowed)
  - The game will start and you can pick your creatures (I'll start with creating 6 different ones to choose from)
  - You can choose a name for yourself
  - The game would be an endless battle til you died.
  	- Your creatures would heal after each battle.
  	- Difficulty would slightly increase each consecutive battle.
  	- Score would be the number of enemy monsters you defeated.
  - Opponent class would be separate from person class, not extending it.
  	- Build AI methods for things like the enemy switching out pokemon.

