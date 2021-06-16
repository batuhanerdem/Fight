import Character
import random


def passives(char):
    char.rage += 5

    if char == Character.kevin:  # Kevin's passive
        critChance = random.randint(1, 5)  # %20 crit change
        if critChance == 5:
            char.crit = True
        else:
            char.crit = False  # when character crits the round before this, if critChance is not 5 which means
            # our char do not crit, this else block changes char.crit back to false.

    if char == Character.fara:  # Fara's passive
        dodgeChance = random.randint(1, 5)
        if dodgeChance == 5:
            char.dodge = True
        else:
            char.dodge = False

    if char == Character.ken:  # Ken's passive
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
        if char == Character.kevin:  # Ken's active passive
            if char.health <= 150:
                char.attack *= 2
                print(f'Kevin passive actived; new attack is {char.attack}')
                char.passive = False

        if char == Character.fara:  # Fara's active passive
            if char.health <= 250:
                char.deffence *= 1.5
                print(f'Fara passive actived; new defence {char.deffence}')
                char.passive = False

        if char == Character.ken:  # Ken's active passive
            if char.health <= 200:
                char.attack += int(char.attack / 2)
                char.deffence += int(char.deffence / 2)
                print(f'Ken passive actived; new attack {char.attack}, new deffence {char.deffence}')
                char.passive = False


def skill(char):
    choice = input(f"Please press 1-2-3 for {char.name}'s skills: ")  # Choising skill

    if char == Character.kevin and choice == "1":  # Kevin's 1. skill gives 5 rage
        char.rage += 5
    if char == Character.kevin and choice == "2":  # Kevin's 2. skill costs 10 rage makes attack 2x
        if char.rage >= 10:
            char.attack *= 2
            char.rage -= 10
            char.skill2 = True
        else:
            print("You dont have enough rage.")
            skill(char)
            return
    if char == Character.kevin and choice == "3":  # Kevin's ult makes attack 4x
        if char.rage >= 50:
            char.attack *= 4
            char.rage -= 50
            char.ult = True
        else:
            print("You dont have enough rage.")
            skill(char)
            return

    if char == Character.fara and choice == "1":  # Fara's 1. skill gives 5 rage
        char.rage += 5
    if char == Character.fara and choice == "2":  # Fara's 2. skill costs 10 rage gives defence
        if char.rage >= 10:
            char.deffence *= 1.5
            char.rage -= 10
            char.skill2 = True
        else:
            print("You dont have enough rage.")
            skill(char)
            return
    if char == Character.fara and choice == "3":  # Fara's ult costs 50 rage and fulls hp
        if char.rage >= 50:
            char.health = 600
            char.rage -= 50
            char.ult = True
        else:
            print("You dont have enough rage.")
            skill(char)
            return
    if char == Character.ken and choice == "1":  # Ken's 1. skill gives 5 rage
        char.rage += 5
    if char == Character.ken and choice == "2":  # Ken's 2. skill costs 10 rage, gives 50 hp and basic attacks
        if char.rage >= 10:
            char.health += 50
            char.skill2 = True
            char.rage -= 10
        else:
            print("You dont have enough rage.")
            skill(char)
            return
    if char == Character.ken and choice == "3":  # Ken's ult costs 50 rage and gives 1.5x attack and deffence
        if char.rage >= 50:
            char.deffence *= 1.5
            char.attack *= 1.5
            char.ult = True
            char.rage -= 50
        else:
            print("You dont have enough rage.")
            skill(char)
            return


def removeEffect(char):
    # This is removing the ult or skill buffs. Health buffs are not included.
    if char.ult:  # Removes ult effects
        if char == Character.kevin:
            char.attack /= 2
        if char == Character.fara:
            pass
        if char == Character.ken:
            char.deffence /= 1.5
            char.attack /= 1.5
        char.ult = False
    if char.skill2:  # Removes skill effects
        if char == Character.kevin:
            char.attack /= 2
        if char == Character.fara:
            char.deffence /= 1.5
        if char == Character.ken:
            pass
        char.skill2 = False
