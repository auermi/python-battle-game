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

    def render_health_bar(person):
        str = ""
        # Always ten cells
        health_percentage = round(person.health / person.MAX_HEALTH * 10)
        for x in range(0, 10):
            if health_percentage > x:
                str += "[•]"
            else:
                str += "[ ]"
        return str
