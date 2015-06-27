import re

class Util:

    def is_valid_input(user_input, pattern):
        try:
            if re.search(pattern, user_input, re.I):
                return True
        except:
            return False
    def printTitle(str):
        str = " %s " % str
        hor = len(str) * "-"
        pls = "+"
        ver = "|"
        return "{}{}{}\n{}{}{}\n{}{}{}\n".format(pls, hor, pls, ver, str, ver, pls, hor, pls)
