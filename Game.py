from Skills import passives
from Skills import skill
from Skills import removeUlt
from Skills import removeSkill
import Features
import Character

global player1Def
global player2Def


def pick():
    # picking character
    select1 = input('Pick a character;\n'
                    '1)Kevin\n'
                    '2)Ken\n'
                    '3)Fara\n')
    select2 = input('Pick a character;\n'
                    '1)Kevin\n'
                    '2)Ken\n'
                    '3)Fara\n')
    if select1 == '1':
        player1 = Character.kevin
    if select1 == '2':
        player1 = Character.ken
    if select1 == '3':
        player1 = Character.fara
    if select2 == '1':
        player2 = Character.kevin
    if select2 == '2':
        player2 = Character.ken
    if select2 == '3':
        player2 = Character.fara

    play(player1, player2)


def game(player1, player2, damage1, damage2):  # thats where damages are calculating
    global player2Def
    global player1Def

    # passive functions that make process about characters passives.
    passives(player1)
    passives(player2)

    # This checks if player1 has ult buff or not. If he has, takes it from him if the buff for 1 round.
    if player1.ult:
        removeUlt(player1)
    if player1.skill2:  # same logic as ult.
        removeSkill(player1)
    skill(player1)
    # Thats where characters are attacking normal, crit or dodging.
    if player2.dodge:  # Dont deal damage if player2.dodge is True which be arranged from passives func.
        print(f"{player2.name} is dodging {player1.name}'s attack")
    elif player1.crit:  # Deal double damage if player1.crit is True which be arranged from passives func.
        print(f"{player1.name} hitting critic attack!")
        print(
            f'{player1.name} hitting {2 * int(player1.attack - (player1.attack * (player2.deffence / 300)))} damage to {player2.name}')
        player2.health -= 2 * int(player1.attack - (player1.attack * (player2.deffence / 300)))
    else:  # Deal normal damage if nothing changed.
        print(
            f'{player1.name} hitting {int(player1.attack - (player1.attack * (player2.deffence / 300)))} damage to {player2.name}')
        player2.health -= int(player1.attack - (player1.attack * (player2.deffence / 300)))
        # loop for print player1's rage

    if player2.health <= 0:
        print(f'{player1.name} WON !!!!!!')
        return

    # Player2 is hitting
    if player2.ult:
        removeUlt(player2)
    if player2.skill2:
        removeSkill(player2)
    skill(player2)
    if player1.dodge:
        print(f"{player1.name} is dodging {player2.name}'s attack")
    elif player2.crit:
        print(f"{player2.name} is hitting critic attack!")
        print(
            f'{player2.name} hitting {2 * int(player2.attack - (player2.attack * (player1.deffence / 300)))} damage to {player1.name}')
        player1.health -= 2 * (int(player2.attack - (player2.attack * (player1.deffence / 300))))
    else:
        print(
            f'{player2.name} hitting {int(player2.attack - (player2.attack * (player1.deffence / 300)))} damage to {player1.name}')
        player1.health -= int(player2.attack - (player2.attack * (player1.deffence / 300)))

    if player1.health <= 0:
        print(f'{player2.name} WON !!!!!!')
        return


def play(player1, player2):
    round = 1
    global player1Def
    global player2Def
    player1Def = 0
    player2Def = 0
   
    while player1.health > 0 and player2.health > 0:
        # player1's health and rage bars
        for number in range(int(player1.health / 4)):  # loop for print player1's health
            print("=", end="")
        print(f"{player1.health} - health")
        for number in range(int(player1.rage / 4)):  # loop for player1's rage
            print("=", end="")
        print(f"{player1.rage} - rage")

        # player2's health and rage bars
        for number in range(int(player2.health / 4)):  # loop for print player2's health
            print("=", end="")
        print(f"{player2.health} - health")
        for number in range(int(player2.rage / 4)):  # loop for player2's rage
            print("=", end="")
        print(f"{player2.rage} - rage")

        print(f'=========ROUND {round}==========')
        game(player1, player2, damage1, damage2)
        round += 1


Features.features()
pick()
