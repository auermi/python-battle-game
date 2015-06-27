import random

class Person(object):

    def __init__(self, health, p_type):
        self.__health = health
        self.__crit_min = 80
        self.__p_type = p_type

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        self.__health = value

    @property
    def p_type(self):
        return self.__p_type

    @p_type.setter
    def p_type(self, value):
        self.p_type = value

    def attack(self, target, max_damage):
        dmg = random.randrange(max_damage/2, max_damage)
        if self.isCrit():
            dmg *= 2
            print("** CRITICAL HIT **")
        target.health -= dmg
        print("{} damage was dealt.".format(dmg))

    def isCrit(self):
        if random.randrange(0, 100) > self.__crit_min:
            return True
        return False

    def isDead(self):
        if self.__health <= 0:
            return True
        return False
