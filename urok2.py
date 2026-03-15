import random

class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.alive = True

    def to_study(self):
        print("Time to study...")
        self.progress += 0.12
        self.gladness -= 5

    def to_sleep(self):
        print("Time to sleep...")
        self.gladness += 3

    def to_chill(self):
        print("Time to chill...")
        self.gladness += 5
        self.progress -= 0.1

    def is_alive(self):
        if self.progress <= -0.5:
            print("Cast out...")
            self.alive = False
        elif self.gladness <= 0:
            print("Depression")
            self.active = False
        elif self.progress >= 5:
            print("Passed externally...")

    def end_of_day(self):
        print(f"Gladness = {self.gladness}")
        print(f"Progress = {self.progress}")

    def live(self, day):
        day = "Day " + str(day) + " of " + self.name + " life"
        print(f"{day:=^50}")
        live_cube = random.randint(1, 3)
        if live_cube == 1:
            self.to_study()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_chill()
        self.end_of_day()
        self.is_alive()

nick = Student(name = "Софія")
for day in range(365):
    if nick.alive == False:
        break
    nick.live(day)