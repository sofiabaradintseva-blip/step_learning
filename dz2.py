import random
from operator import truediv


class Human:
    def __init__(self, name="Human", job=None, home=None, car=None, pet=None):
        self.name = name
        self.money = 100
        self.gladness = 50
        self.safety = 50
        self.job = job
        self.home = home
        self.car = car
        self.pet = pet

    def get_home(self):
        self.home = House()

    def get_car(self):
        self.car = Auto(brands_of_car)

    def get_job(self):
        if self.car.drive():
            pass
        else:
            self.to_repair()
            return
        self.job = Job(job_list)

    def get_pet(self):
        self.pet = Pet(name_of_pet)

    def eat(self):
        if self.home.food <= 0:
            self.shopping('food')
        else:
            if self.safety >= 100:
                self.safety = 100
                return
            self.safety += 5
            self.home.food -= 5

    def work(self):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                self.shopping("fuel")
                return
            else:
                self.to_repair()
                return
            self.money += self.job.salary
            self.gladness -= self.job.gladness_less
            self.safety -= 4

    def shopping(self, manage):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                manage = "fuel"
            else:
                self.to_repair()
                return
        if manage == "fuel":
            print("Купуємо паливо...")
            self.money -= 100
            self.car.fuel += 100
        elif manage == "food":
            print("Купуємо продукт...")
            self.money -= 50
            self.home.food += 50
        elif manage == "delicies":
            print("Купуємо делікатеси...")
            self.money -= 15
            self.gladness += 10
            self.safety += 2

    def chill(self):
        self.gladness += 10
        self.home.mess += 5

    def clean_home(self):
        self.gladness -= 5
        self.home.mess = 0

    def to_repair(self):
        self.car.strenth += 100
        self.money -= 50

    def walk_with_pet(self):
        self.pet.walk()
        self.is_pet_want_to_eat()

    def is_pet_want_to_eat(self):
        if self.pet.want_to_eat():
            self.pet.eat()
            self.money -= 20

    def go_to_pet_doctor(self):
        self.pet.visit_doctor()
        self.money -= 40
        self.gladness -= 10

    def need_a_pet_doctor(self):
        if self.pet.need_a_doctor():
            self.go_to_pet_doctor()
        else:
            print("Цуцик у порядку. Доктор не треба")

    def days_index(self, day):
        day = f" Сьогодні {day} з життя {self.name} "
        print(f"{day:=^50}", "\n")
        human_indexes = self.name + " життя"
        print(f"{human_indexes:=^50}", "\n")
        print(f"Money - {self.money}")
        print(f"Satiety - {self.safety}")
        print(f"Gladness - {self.gladness}")
        home_indexes = "Показники дому"
        print(f"{home_indexes:=^50}", "\n")
        print(f"Food - {self.home.food}")
        print(f"Mess - {self.home.mess}")
        car_indexes = f"{self.car.brand} показники авто"
        print(f"{car_indexes:=^50}", "\n")
        print(f"Fuel - {self.car.fuel}")
        print(f"Strength - {self.car.strength}")
        pet_indexes = f"Показники собаки {self.pet.name}"
        print(f"{pet_indexes:=^50}", "\n")
        print(f"Health - {self.pet.health}")
        print(f"Satiety - {self.pet.satiety}")

    def is_alive(self):
        if self.gladness < 0:
            print("Depression...")
            return False
        if self.safety < 0:
            print("Dead...")
            return False
        if self.money < -500:
            print("Bankrupt...")
            return False
    def live(self, day):
        if self.is_alive() == False:
            return False
        if self.home is None:
            print("Settled in the house")
            self.get_home()
        if self.car is None:
            self.get_car()
            print(f"I bought a car {self.car.brand}")
        if self.job is None:
            self.get_job()
            print(f"I don't have a job, going to get a job {self.job.job} with salary {self.job.salary}")
        if self.pet is None:
            self.get_pet()
            print(f"Купив собі собаку. Назвав {self.pet.name}")
        self.days_index(day)
        dice = random.randint(1, 4)
        if self.safety < 20:
            print("I'll go eat")
            self.eat()
        elif self.gladness < 20:
            if self.home.mess > 15:
                print("I want to chill, but there is so much mess...\n So I will clean the house")
                self.clean_home()
            else:
                print("Let`s chill!")
                self.chill()
        elif self.money < 0:
            print("Start working")
            self.work()
        elif self.car.strength < 15:
            print("I need to repair my car")
            self.to_repair()
        elif dice == 1:
            print("Let`s chill!")
            self.chill()
        elif dice == 2:
            print("Start working")
            self.work()
        elif dice == 3:
            print("Cleaning time!")
            self.clean_home()
        elif dice == 4:
            print("Time for treats!")
            self.shopping(manage="delicacies")

        print("Time to walk with dog")
        self.walk_with_pet()
        self.need_a_pet_doctor()

class Auto:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.fuel = brand_list[self.brand]["fuel"]
        self.strength = brand_list[self.brand]["strength"]
        self.consumption =brand_list[self.brand]["consumption"]

    def drive(self):
        if self.strength > 0 and self.fuel >= self.consumption:
            self.fuel -= self.consumption
            self.strength -= 1
            return True
        else:
            print("The car cannot move")
            return False

class House:
    def __init__(self):
        self.mess = 0
        self.food = 0

class Pet:
    def __init__(self, name):
        self.name = name
        self.health = 50
        self.satiety = 50

    def want_to_eat(self):
        if self.satiety <= 10:
            print("Собаці треба поїсти...")
            return True
        return False

    def need_a_doctor(self):
        if self.health <= 20 or self.satiety >= 100:
            print("Собаці треба до лікаря...")
            return True
        return False

    def eat(self):
        print("Собака їсть...")
        self.satiety += 10

    def visit_doctor(self):
        print("Собака на візиті у лікаря")
        self.health = 50
        self.satiety = 50

    def walk(self):
        print("Собака гуляє")
        self.satiety -= 10
        with_trauma = random.randint(0, 1)
        if with_trauma == 1:
            print("Собака травмувалась на прогулянці")
            self.health -= 10
        else:
            self.health -= 1

job_list = {
"Java developer":
{"salary":50, "gladness_less": 10 },
"Python developer":
{"salary":40, "gladness_less": 3 },
"C++ developer":
{"salary":45, "gladness_less": 25 },
"Rust developer":
{"salary":70, "gladness_less": 1 },
}
brands_of_car = {
"BMW":{"fuel":100, "strength":100,
"consumption": 6},
"Lada":{"fuel":50, "strength":40,
"consumption": 10},
"Volvo":{"fuel":70, "strength":150,
"consumption": 8},
"Ferrari":{"fuel":80, "strength":120,
"consumption": 14},
}

names_of_pet = ["Чак", "Артемон", "Бурулька", "Шарик"]
random_index = random.randint(0,3)
name_of_pet = names_of_pet[random_index]

class Job:
    def __init__(self, job_list):
        self.job = random.choice(list(job_list))
        self.salary = job_list[self.job]["salary"]
        self.gladness_less = job_list[self.job]["gladness_less"]

nick = Human(name="Nick")
for day in range(1,8):
    if nick.live(day) == False:
        break