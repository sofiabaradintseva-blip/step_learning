import random

class Pet:
    def __init__(self, name):
        self.name = name
        self.energy = 10
        self.satiety = 0
        self.water = 0

    def walk(self):
        self.is_hungry()
        self.is_want_to_drink()
        self.energy -= 10
        self.satiety -= 1
        self.water -= 2
        print("Walking...")

    def drink(self):
        self.water = 10
        self.energy += 5
        print("Drinking...")

    def eat(self):
        self.satiety = 10
        self.energy += 10
        print("Eating...")

    def sleep(self, minutes):
        self.is_hungry()
        self.is_want_to_drink()
        self.energy += minutes * 0.1
        self.satiety -= minutes * 0.1
        self.water -= minutes * 0.1
        print(f"Sleeping {minutes} minutes...")

    def play(self, minutes):
        self.is_hungry()
        self.is_want_to_drink()
        self.energy -= minutes * 0.5
        self.satiety -= minutes
        self.water -= minutes
        print(f"Playing {minutes} minutes...")
        if self.energy <= 0:
            self.sleep(30)

    def is_hungry(self):
        if self.satiety <= 0:
            print("Time to eat...")
            self.eat()

    def is_want_to_drink(self):
        if self.water <= 0:
            print("Time to drink...")
            self.drink()

    def end_of_the_day(self):
        print(f"Energy = {self.energy}")
        print(f"Satiety = {self.satiety}")
        print(f"Watering = {self.water}")

    def day(self):
        minutes_of_day = 24 * 60
        while minutes_of_day > 0:
            action = random.randint(1, 3)
            if action == 1:
                self.walk()
                minutes_of_day -= 10
            elif action == 2:
                play_minutes = random.randint(20, 60)
                self.play(play_minutes)
                minutes_of_day -= play_minutes
            elif action == 3:
                sleep_minutes = random.randint(30, 120)
                self.sleep(sleep_minutes)
                minutes_of_day -= sleep_minutes
            self.is_hungry()
            self.is_want_to_drink()
            minutes_of_day -= 1
        self.end_of_the_day()

our_pet = Pet('Chak')
for day in range(7):
    day_string = "----Day " + str(day) + " of " + our_pet.name + " life----"
    print(f"{day_string:50}")
    our_pet.day()