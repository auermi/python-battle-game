import random

class person(object):

    def __init__(self, health, defense):
        self.__health = health
        self.__crit_min = 80

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        self.health = value

    def attack(target, max_damage):
        dmg = random.randrange(max_damage/2, max_damage)
        if isCrit():
            dmg *= 2
            print("** CRITICAL HIT **")
        target.health -= dmg
        print("{} damage was dealt.".format(dmg))

    def isCrit():
        if random.randrange(0, 100) > crit_min:
            return True
        return False
