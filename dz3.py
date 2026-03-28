import random

class Action:
    def __init__(self, is_attack, napr_attack=None, power_of_attack=0, is_block=False, napr_block=None):
        self.is_attack = is_attack
        self.is_block = is_block
        self.power_of_attack = power_of_attack
        self.napr_attack = napr_attack
        self.napr_block = napr_block

class Warrior:
    def __init__(self, weapon):
        self.health = 100
        self.strength = 50
        self.protection = 100
        self.weapon = weapon
        self.last_action = None
        self.name = "Лицар"

    def get_attack_napr(self):
        napr = random.randint(0,1)
        return napr

    def get_attack_power(self):
        power = random.randint(1, self.strength)
        return power

    def get_block_napr(self):
        napr = random.randint(0, 1)
        return napr

    def get_napr_text(self, napr):
        if napr == 0:
            napr_text = 'верх'
        else:
            napr_text = 'низ'
        return napr_text

    def action(self):
        type = random.randint(0,1)
        if type == 0:
            napr = self.get_attack_napr()
            power = self.get_attack_power()
            print(f"Атакую {self.get_napr_text(napr)} з силою {power}")
            action = Action(True, napr, power, False)
        else:
            napr = self.get_block_napr()
            print(f"Блокую {self.get_napr_text(napr)}")
            action = Action(False, None, 0, True, napr)
        self.last_action = action
        return action

    def is_alive(self):
        return self.health > 0

    def calculate_damage(self, action):
        if action.is_attack:
            if self.last_action.is_block:
                if action.napr_attack == self.last_action.napr_block and self.protection >= action.power_of_attack:
                    print(f"Блокую атаку...")
                    self.protection -= action.power_of_attack
                    print(f"Залишилось {self.protection} броні")
                elif action.napr_attack == self.last_action.napr_block and self.protection < action.power_of_attack:
                    if self.protection > 0:
                        print("Не можу повністю заблокувати удар")
                        self.health -= action.power_of_attack - self.protection
                        self.protection = 0
                        print("Броні більше нема")
                        print(f"Здоров'я залишилось {self.health}")
                    else:
                        self.health -= action.power_of_attack
                        print(f"Здоров'я залишилось {self.health}")
                else:
                    self.health -= action.power_of_attack
                    print(f"Здоров'я залишилось {self.health}")
            else:
                self.health -= action.power_of_attack
                print(f"Здоров'я залишилось {self.health}")

class Dwarf(Warrior):
    def __init__(self, weapon):
        super().__init__(self)
        self.name = "Гном"
        self.health = 200
        self.protection = 0
        self.strength = 300
        self.weapon = weapon

class Elf(Warrior):
    def __init__(self, weapon):
        super().__init__(self)
        self.health = 500
        self.protection = 1000
        self.strength = 5
        self.name = "Ельф"
        self.weapon = weapon

    def calculate_damage(self, action):
        if action.is_attack:
            if self.last_action.is_block:
                if self.protection >= action.power_of_attack:
                    print(f"Блокую атаку...")
                    self.protection -= action.power_of_attack
                    print(f"Залишилось {self.protection} броні")
                elif self.protection < action.power_of_attack:
                    if self.protection > 0:
                        print("Не можу повністю заблокувати удар")
                        self.health -= action.power_of_attack - self.protection
                        self.protection = 0
                        print("Броні більше нема")
                        print(f"Здоров'я залишилось {self.health}")
                    else:
                        self.health -= action.power_of_attack
                        print(f"Здоров'я залишилось {self.health}")
                else:
                    self.health -= action.power_of_attack
                    print(f"Здоров'я залишилось {self.health}")
            else:
                self.health -= action.power_of_attack
                print(f"Здоров'я залишилось {self.health}")

    def get_napr_text(self, napr):
        return ''

type1 = random.randint(1,3)
type2 = random.randint(1,3)
if type1 == 1:
    igr1 = Warrior("Меч")
elif type1 == 2:
    igr1 = Dwarf("Топор")
else:
    igr1 = Elf("Лук")

if type2 == 1:
    igr2 = Warrior("Меч")
elif type2 == 2:
    igr2 = Dwarf("Топор")
else:
    igr2 = Elf("Лук")

print("Вітаємо на нашій арені. Сьогоді пройде турнір між двома видатними бійцями")
print("До вашої уваги ігрок 1:")
print(igr1.name)
print(f"Його зброя - {igr1.weapon}")
print(f"Його сила - {igr1.strength}")
print(f"Його броня - {igr1.protection}")
print(f"Його здоров'я - {igr1.health}")
print("==================================================")
print("До вашої уваги ігрок 2:")
print(igr2.name)
print(f"Його зброя - {igr2.weapon}")
print(f"Його сила - {igr2.strength}")
print(f"Його броня - {igr2.protection}")
print(f"Його здоров'я - {igr2.health}")
print("==================================================")
input("Натисніть ентер для початку бою")

round = 1
while igr1.is_alive() & igr2.is_alive():
    print(f"Round {round:=^50}")
    print(f"{igr1.name} 1 каже:")
    igr1_action = igr1.action()
    print(f"{igr2.name} 2 каже:")
    igr2_action = igr2.action()
    print(f"{igr1.name} 1 каже:")
    igr1.calculate_damage(igr2_action)
    if not igr1.is_alive():
        print(f"{igr1.name} 1 помер")
    print(f"{igr2.name} 2 каже:")
    igr2.calculate_damage(igr1_action)
    if not igr1.is_alive():
        print(f"{igr2.name} 2 помер")
    round += 1