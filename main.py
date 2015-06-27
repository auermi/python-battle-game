# Special thanks to Waseem Dahman (@wsmd) for help util.is_valid_input && util.printTitle

from game import Game
from util import Util

util = Util

while True:
    Game.init_game()
    # Space after break out of loop and end game
    print("\n")
    print ("Would you like to play again? (yes/no)")
    resp = input("> ")
    if (util.is_valid_input(resp, "no")):
        break
    print("\n")
