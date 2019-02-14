import random
from classes.magic import Spell

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Person:
    """Define the stats of the object"""
    def __init__(self, name, hp, mp, atk, df, magic, items):
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atkh = atk + 10
        self.atkl = atk - 10
        self.df = df
        self.magic = magic
        self.action = ["Attack", "Magic", "Items"]
        self.items = items
        self.name = name

    """Defining utility functions"""
    def generate_damage(self):
        return random.randrange(self.atkl, self.atkh)

    def heal(self, heal):
        self.hp += heal
        if self.hp >= self.maxhp:
            self.hp = self.maxhp

    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp <= 0:
            self.hp = 0
        return self.hp

    def get_hp(self):
        return self.hp

    def get_maxhp(self):
        return self.maxhp

    def get_mp(self):
        return self.mp

    def get_maxmp(self):
        return self.maxmp

    def reduce_mp(self, cost):
        self.mp -= cost

    def choose_action(self):
        i = 1
        print(" Pick an ACTION for", self.name, ":")
        for item in self.action:
            print("    " + str(i) + ": ", item)
            i += 1

    def choose_spell(self):
        i = 1
        print("SPELLS")
        for spell in self.magic:
            print("    " + str(i), ": ", spell.name, "(", str(spell.cost), "mp)")
            i += 1

    def choose_items(self):
        i = 1
        print("ITEMS")
        for item in self.items:
            print("    " + str(i) + ".", item.name, ":", item.description, "(x" + str(item.quantity) + ")")
            i += 1

    def get_stats(self):
        hp_bar = ""
        bar_ticks = (self.hp / self.maxhp) * 15
        compensation = (15 - bar_ticks)/2

        while bar_ticks >= 1:
            hp_bar += "█"
            bar_ticks -= 1

        while len(hp_bar) < (15+compensation):
            hp_bar += " "

        print("                        " + bcolors.OKGREEN + "_________________________" + bcolors.ENDC +
              "                " + bcolors.OKBLUE + "_________" + bcolors.ENDC)

        print(bcolors.BOLD + str(self.name) + "   " + str(self.hp) + "/" + str(self.maxhp)
              + bcolors.OKGREEN + "     |" + hp_bar + "|" + bcolors.ENDC + "     " + str(self.mp) + "/"
              + str(self.maxmp) + bcolors.OKBLUE + "     |█████|" + bcolors.ENDC)
