class Hero:
    def __init__(self, name: str, health: int, mana:int):
        self.name = name
        self.health = health
        self.mana = mana

    def cast(self, hero_name: str, mana_needed: int, spell_name: str):
        if self.mana >= mana_needed:
            print(f"{hero_name} has successfully cast {spell_name} and now has {self.mana - mana_needed} MP!")
            self.mana -= mana_needed
        else:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")

    def take_dmg(self, hero_name: str, dmg: int, attacker: str):
        if self.health - dmg > 0:
            print(f"{hero_name} was hit for {dmg} HP by {attacker} and now has {self.health - dmg} HP left!")
            self.health -= dmg
        else:
            print(f"{hero_name} has been killed by {attacker}!")
            self.name = None
            self.health = None
            self.mana = None

    def recharge(self, hero_name: str,  amount: int):
        mana_waste = 0
        if self.mana + amount >= 200:
            mana_waste = self.mana + amount - 200
        mana_recovered = amount - mana_waste
        self.mana += mana_recovered
        print(f"{hero_name} recharged for {mana_recovered} MP!")    #MAY HAVE A BUG HERE

    def heal(self, hero_name: str, amount: int):
        health_waste = 0
        if self.health + amount >= 100:
            health_waste = self.health + amount - 100
        health_recovered = amount - health_waste
        self.health += health_recovered
        print(f"{hero_name} healed for {health_recovered} HP!")

    def display_hero(self):
        print(self.name)
        print(f"  HP: {self.health}")
        print(f"  MP: {self.mana}")


def hero_by_name(name: str, heroes: list):
    for hero in heroes:
        if hero.name == name:
            return hero


n = int(input())
heroes = []
for _ in range(n):
    hero_info = input().split()
    name = hero_info[0]
    mana = int(hero_info[1])
    health = int(hero_info[2])
    heroes.append(Hero(name, mana, health))

while True:
    command = input().split(" - ")
    command_name = command[0]

    if command_name == "End":
        break

    hero_name = command[1]
    hero = hero_by_name(hero_name, heroes)
    if command_name == "CastSpell":
        mp_needed = int(command[2])
        spell_name = command[3]
        hero.cast(hero_name, mp_needed, spell_name)

    elif command_name == "TakeDamage":
        damage = int(command[2])
        attacker = command[3]
        hero.take_dmg(hero_name, damage, attacker)

    elif command_name == "Recharge":
        amount = int(command[2])
        hero.recharge(hero_name, amount)

    else:
        amount = int(command[2])
        hero.heal(hero_name, amount)

for hero in heroes:
    if hero.name is not None:
        hero.display_hero()
