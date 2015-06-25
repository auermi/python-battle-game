import re
from util import Util

from person import Person

util = Util


player = Person(100, "player")
enemy = Person(100, "enemy")
print("arena-battle.py")
print("Hello, and welcome to the arena. In order to survive you must defeat your opponent.")

while True:
    # Player attack phase
    print("Enter the respective command to take an action:\n[1] Attack")
    action = input("> ")
    if util.is_valid_input(action, "attack"):
        player.attack(enemy, 10)
        print ("Your opponent has {} health left".format(enemy.health))
    elif util.is_valid_input(action, "quit"):
        break
    else:
        print ("Invalid input please try again.")

    # Enemy Attack Phase
    enemy.attack(player, 10)
    print ("You have {} health left.".format(player.health))

    
