class Character():
    def __init__(self, name, attack, deffence, health, passive=True, crit=False, dodge=False, rage=0, skill2=False,
                 ult=False):
        self.name = name
        self.attack = attack
        self.deffence = deffence
        self.health = health
        self.passive = passive
        self.crit = crit
        self.dodge = dodge
        self.rage = rage
        self.skill2 = skill2
        self.ult = ult


kevin = Character('kevin', 80, 25, 300)
fara = Character('fara', 30, 80, 600)
ken = Character('ken', 50, 50, 400)
