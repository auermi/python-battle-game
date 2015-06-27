from util import Util
from person import Person

class Game:

    def init_game ():
        util = Util

        player = Person(100, "player")
        enemy = Person(100, "enemy")
        print(util.printTitle("arena-battle.py"))
        print("Hello, and welcome to the arena. In order to survive you must defeat your opponent.")

        while True:
            # Player attack phase
            print("\nEnter the respective command to take an action:\n\n    [ ] Attack\n    [ ] Quit\n")
            action = input("> ")
            print("")
            if util.is_valid_input(action, "attack"):
                player.attack(enemy, 10)
                if enemy.isDead():
                    print("\nYou are the victor! Congratulations, you have won the game!")
                    break
                print ("Your opponent has {} health left\n".format(enemy.health))
            elif util.is_valid_input(action, "quit"):
                break
            else:
                print ("Invalid input please try again.")

            # Enemy Attack Phase
            print("Your opponent is attacking you.")
            enemy.attack(player, 10)
            if player.isDead():
                print("\nYou were killed in the arena! You have lost this game.")
                break

            print("You have {} health left.".format(player.health))
