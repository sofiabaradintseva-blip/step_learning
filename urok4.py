'''
class Animal:
    def __init__(self, name):
        self.name = name
        print(f"Тварина {self.name} створена")

    def speak(self):
        print("Тварина видає звук")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
        print(f"Собака породи {self.breed} створена!")

    def speak(self):
        super().speak()
        print("Гав, гав!")

class Cat(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
        print(f"Кіт породи {self.breed} створена!")

    def speak(self):
        super().speak()
        print("Мяу, мяу!")

dog = Dog("Чак", "Йоркширський терьєр")
dog.speak()
cat = Cat("Мурчик", "Мейкун")
cat.speak()
'''

class Character:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        print(f"{self.name} created with HP {self.hp}")

    def attack(self):
        print("Character is attacking!")

class Warrior(Character):
    def __init__(self, name, hp, weapon):
        super().__init__(name, hp)
        self.weapon = weapon

    def attack(self):
        super().attack()
        print(f"Attacking with {self.weapon}")

class Mage(Character):
    def __init__(self, name, hp, magic):
        super().__init__(name, hp)
        self.magic = magic

    def attack(self):
        super().attack()
        print(f"Attcking with {self.magic}")

class Elf(Warrior):
    def __init__(self, name, hp, count_arrow):
        super().__init__(name, hp, 'bow')
        self.count_arrow = count_arrow

    def attack(self):
        super().attack()
        self.count_arrow -= 1
        print(f"{self.name} left {self.count_arrow} arrows")

w = Warrior("Artur", 100, "sword")
m = Mage("Merlin", 80, "Fire")
e = Elf("Legolas", 120, 100)
w.attack()
m.attack()
e.attack()