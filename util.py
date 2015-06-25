import re

class Util:
    def validateInput(test_case, inpt):
        if re.search(test_case, inpt, flags=re.IGNORECASE):
            return True
