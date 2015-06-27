from util import Util
from person import Person

class Game:

    def init_game ():
        util = Util

        player = Person(100, "player", 3)
        enemy = Person(100, "enemy", 3)
        print(util.printTitle("arena-battle.py"))
        print("Hello, and welcome to the arena. In order to survive you must defeat your opponent.")

        def player_attack_phase():
            # Player attack phase
            print("\nEnter the respective command to take an action:\n\n    [ ] Attack\n    [ ] Check Health\n    [ ] Quit")
            action = input("\n> ")
            print("")
            if util.is_valid_input(action, "attack"):
                player.attack(enemy, 10)
                if enemy.isDead():
                    print("\nYou are the victor! Congratulations, you have won the game!")
                    return False
                print ("Your opponent has {} health left\n".format(enemy.health))
            elif util.is_valid_input(action, "quit"):
                return False
            elif util.is_valid_input(action, "check health"):
                print("Player: {} health\n".format(player.health))
                return player_attack_phase()
            else:
                print ("Invalid input please try again.\n")
                return player_attack_phase()
            return True

        while True:

            if not player_attack_phase():
                break

            # Enemy Attack Phase
            print("Your opponent is attacking you.")
            enemy.attack(player, 10)
            if player.isDead():
                print("\nYou were killed in the arena! You have lost this game.")
                break

            print("You have {} health left.".format(player.health))
