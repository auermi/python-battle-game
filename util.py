import re

class Util:
    def is_valid_input(test_case, inpt):
        if re.search(test_case, inpt, re.I):
            return True
