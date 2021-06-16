import Character
import random


def passives(char):
    # char.rage += random.randint(10, 25)
    char.rage += 5

    if char == Character.kevin:
        critChance = random.randint(1, 5)  # %20 crit change
        if critChance == 5:
            char.crit = True
        else:
            char.crit = False  # when character crits the round before this, if critChance is not 5 which means
            # our char do not crit, this else block changes char.crit back to false.

    if char == Character.fara:
        dodgeChance = random.randint(1, 5)
        if dodgeChance == 5:
            char.dodge = True
        else:
            char.dodge = False

    if char == Character.ken:
        critChance = random.randint(1, 5)
        dodgeChance = random.randint(1, 5)
        if critChance == 5:
            char.crit = True
        else:
            char.crit = False
        if dodgeChance == 5:
            char.dodge = True
        else:
            char.dodge = False

    if char.passive:
        if char == Character.kevin:
            if char.health <= 150:
                char.attack *= 2
                print(f'Kevin passive actived; %100 crit chance on')
                char.passive = False

        if char == Character.fara:
            if char.health <= 250:
                char.deffence *= 1.5
                print(f'Fara passive actived; new defence {char.deffence}')
                char.passive = False

        if char == Character.ken:
            if char.health <= 200:
                char.attack += int(char.attack / 2)
                char.deffence += int(char.deffence / 2)
                print(f'Ken passive actived; new attack {char.attack}, new deffence {char.deffence}')
                char.passive = False


def skill(char):
    choice = input(f"Please press 1-2-3 for {char.name}'s skills: ")  # Choising skill

    if char == Character.kevin and choice == "1":  # Kevins 1. skill gives 5 rage
        char.rage += 5
    if char == Character.kevin and choice == "2":  # Kevins 2. skill takes 10 rage
        if char.rage >= 10:
            char.attack *= 2
            char.skill2 = True
            char.rage -= 10
        else:
            print("You dont have enough rage.")
            skill(char)
            return
    if char == Character.kevin and choice == "3":  # Kevins ult.
        if char.rage >= 50:
            char.attack *= 4
            char.rage -= 50
            char.ult = True
        else:
            print("You dont have enough rage.")
            skill(char)
            return

    if char == Character.fara and choice == "1":
        char.rage += 5
    if char == Character.fara and choice == "2":
        if char.rage >= 10:
            char.deffence *= 1.5
            char.skill2 = True
            char.rage -= 10
        else:
            print("You dont have enough rage.")
            skill(char)
            return
    if char == Character.fara and choice == "3":
        if char.rage >= 50:
            char.health = 600
            char.rage -= 50
            char.ult = True
        else:
            print("You dont have enough rage.")
            skill(char)
            return
    if char == Character.ken and choice == "1":
        char.rage += 5
    if char == Character.ken and choice == "2":
        if char.rage >= 10:
            char.health += 50
            char.skill2 = True
            char.rage -= 10
        else:
            print("You dont have enough rage.")
            skill(char)
            return
    if char == Character.ken and choice == "3":
        if char.rage >= 50:
            char.deffence *= 1.5
            char.attack *= 1.5
            char.ult = True
            char.rage -= 50
        else:
            print("You dont have enough rage.")
            skill(char)
            return


def removeUlt(char):
    # This is removing the ult effect for 1 round ults like Kevin's and Ken's.
    # This func is taking buffs from them the round after they used ults.
    if char == Character.kevin:
        char.attack /= 2
    if char == Character.fara:
        pass
    if char == Character.ken:
        char.defence /= 1.5
        char.attack /= 1.5
    char.ult = False


def removeSkill(char):
    # This is removing the skill effect for 1 round skills.
    # This func is taking buffs from them the round after they used skills.
    if char == Character.kevin:
        char.attack /= 1.5
    if char == Character.fara:
        char.deffence /= 1,5
    if char == Character.ken:
        pass
    char.skill2 = False
