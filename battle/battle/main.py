from classes.game import Person, bcolors
from classes.magic import Spell
from classes.inventory import Item

"""
print("\n\n")
print("NAME               HP                                   MP")

print("                  " + bcolors.OKGREEN + "_________________________" + bcolors.ENDC +
      "             " + bcolors.OKBLUE + "_________" + bcolors.ENDC)

print(bcolors.BOLD + "Valos:   460/460 "
      + bcolors.OKGREEN + " |███████████████|" + bcolors.ENDC + "     65/65 "
      + bcolors.OKBLUE + " |█████|" + bcolors.ENDC)

print("                  _________________________             _________")
print("Valos:   460/460  |███████████████|     65/65  |█████|")
print("\n\n")
"""

# Create Black Magic
fire = Spell("Fire", 10, 100, "black")
thunder = Spell("Thunder", 10, 100,"black")
blizzard = Spell("Blizzard", 10, 100, "black")
meteor = Spell("Meteor", 20, 200, "black")
quake = Spell("Quake", 14, 140, "black")

# Create White Magic
cure = Spell("Cure", 12, 120, "white")
cura = Spell("Cura", 18, 200, "white")

# Create some Items
potion = Item("Potion", "potion", "Heals 50 HP", 50)
hipotion = Item("Hi-Potion", "potion", "Heal 100 HP", 100)
superpotion = Item("Super Potion", "potion", "Heals 500 HP", 500)

elixer = Item("Elixer", "elixer", "Fully restore HP/MP of the target", 9999)
hielixer = Item("MegaElixer", "elixer", "Fully restore HP/MP of the party", 9999)

grenade = Item("Grenade", "attack", "Deals 500 damage", 500)

player_spells = [fire, thunder, blizzard, meteor, quake, cure, cura]
player_items = [potion, hipotion, superpotion, elixer, hielixer, grenade]
player_quantity = [15, 5, 3, 3, 1, 5]

i = 0
for items in player_items:
    items.set_quantity(player_quantity[i])
    i += 1


# Instantiate Persons
player = Person("1: Valos:", 460, 65, 60, 34, player_spells, player_items)
player2 = Person("2: Maria:", 460, 65, 60, 34, player_spells, player_items)
player3 = Person("3: Azur :", 460, 65, 60, 34, player_spells, player_items)
enemy = Person("Hanzo:", 850, 65, 45, 25, [], [])

players = [player, player2, player3]

running = True
print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKS!" + bcolors.ENDC)

while running:
    """ Initiation of the graphical chart """
    print("=======================================================================")
    print("NAME                  HP                                      MP")
    for player in players :
        player.get_stats()
    print("\n")

    """ Selection of the player """
    choice = input("Choose a hero : ")
    player = players[int(choice) - 1]

    """ User select his next action """
    player.choose_action()
    choice = input("\nChoose action: ")
    index_action = int(choice)-1
    print("You chose :", player.action[index_action], ".")

    if index_action == 0:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print("--------------------")
        print(bcolors.OKBLUE + "You attacked for", dmg, "points of damage.\n" + bcolors.ENDC)

    elif index_action == 1:
        player.choose_spell()
        choice = input("\nChoose spell: ")

        if int(choice) == 0:
            continue

        spell = player.magic[int(choice) - 1]
        print("You chose:", spell.name, ".")

        if player.get_mp() >= spell.cost:
            dmg = spell.generate_damage()

            if spell.type == "white":
                player.heal(dmg)
                print("--------------------")
                print(bcolors.OKGREEN + "You healed yourself with", spell.name, "for", dmg, "hp." + bcolors.ENDC)
            else:
                enemy.take_damage(dmg)
                print("--------------------")
                print(bcolors.OKBLUE + "You attacked with", spell.name, "for", dmg, "points of damage." + bcolors.ENDC)

            player.reduce_mp(spell.cost)

        else:
            print(bcolors .FAIL + "You fail to cast your spell because your mp are too low !" + bcolors.ENDC)

    elif index_action == 2:
        player.choose_items()
        choice = input("\nChoose item: ")

        if int(choice) == 0:
            print("test")
            continue

        item = player.items[int(choice) - 1]
        item.quantity -= 1

        if item.quantity < 0:
            item.quantity = 0
            print(bcolors .FAIL + "You look hard but can't find this item !" + bcolors.ENDC)
            continue

        if item.type == "potion":
            player.heal(item.prop)
            print(bcolors.OKGREEN + item.name + " heals for", str(item.prop), "HP" + bcolors.ENDC)

        elif item.type == "elixer":
            player.hp = player.maxhp
            player.mp = player.maxmp
            print(bcolors.OKGREEN + item.name + " fully restored your HP/MP" + bcolors.ENDC)

        elif item.type == "attack":
            enemy.take_damage(item.prop)
            print(bcolors.OKBLUE + item.name + " deals " + str(item.prop) + "points of damage.")

    else:
        print("Please enter a number corresponding to a displayed option.\n")

    if enemy.get_hp() == 0:
        print(bcolors.OKGREEN + "Enemy HP:" + str(enemy.get_hp()) + "." + bcolors.ENDC)
        print(bcolors.OKGREEN + "You win!" + bcolors.ENDC)
        running = False
        continue

    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print(bcolors.FAIL + "Enemy attacks for", enemy_dmg, "points of damage.\n" + bcolors.ENDC)

    print(bcolors.OKGREEN + "Player HP:" + str(player.get_hp()) + "/" + str(player.maxhp) + bcolors.ENDC)
    print(bcolors.OKGREEN + "Player MP:" + str(player.get_mp()) + "/" + str(player.maxmp) + bcolors.ENDC)
    print(bcolors.FAIL + "Enemy HP :" + str(enemy.get_hp()) + "/" + str(enemy.maxhp) + bcolors.ENDC)

    if player.get_hp() == 0:
        print(bcolors.FAIL + "Your enemy has defeated you !" + bcolors.ENDC)
        running = False
        continue
