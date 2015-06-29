import random
from util import Util

util = Util


class Person(object):

    def __init__(self, health, p_type, defense):
        self.__health = health
        self.__MAX_HEALTH = health
        self.__p_type = p_type
        self.__defense = defense

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        self.__health = value

    @property
    def MAX_HEALTH(self):
        return self.__MAX_HEALTH

    @property
    def p_type(self):
        return self.__p_type

    @p_type.setter
    def p_type(self, value):
        self.p_type = value

    @property
    def defense(self):
        return self.__defense

    @defense.setter
    def defense(self, value):
        self.defense = value

    def attack(self, target, action):
        max_damage = 0
        if util.is_valid_input(action, "stab"):
            max_damage = 10
        elif util.is_valid_input(action, "punch"):
            max_damage = 5
        elif util.is_valid_input(action, "fireball"):
            max_damage = 15
        else:
            print("type: -> {}        max)_damage -> {}".format(type, max_damage))

        dmg = random.randrange(round(max_damage/2), max_damage)
        if self.isCrit(type):
            dmg *= 2
            print("** CRITICAL HIT **")
        if dmg > self.__defense:
            target.health -= dmg + self.__defense
            print("{} damage was dealt.".format(dmg))
        else:
            print("0 damage was dealt.")

    def isCrit(self, action):
        crit_min = 0
        if type == "stab":
            crit_min = 80
        elif type == "punch":
            crit_min =  70
        elif type == "fireball":
            max_damage = 85
        if random.randrange(0, 100) > crit_min:
            return True
        return False

    def isDead(self):
        if self.__health <= 0:
            return True
        return False
