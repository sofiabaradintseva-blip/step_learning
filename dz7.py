import random
import logging

logging.basicConfig(
    filename="life_simulation.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Програма симуляції запущена")


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
        logging.info("Оселився в будинку")

    def get_car(self):
        self.car = Auto(brands_of_car)
        logging.info(f"Купив авто {self.car.brand}")

    def get_job(self):
        try:
            if self.car.drive():
                self.job = Job(job_list)
                logging.info(
                    f"Отримав роботу {self.job.job} "
                    f"із зарплатою {self.job.salary}"
                )
            else:
                self.to_repair()

        except Exception:
            logging.exception("Помилка отримання роботи")

    def get_pet(self):
        self.pet = Pet(name_of_pet)
        logging.info(f"Купив собаку {self.pet.name}")

    def eat(self):
        if self.home.food <= 0:
            logging.warning("Немає їжі — купуємо")
            self.shopping('food')
        else:
            self.safety += 5
            self.home.food -= 5
            logging.info("Поїв")

    def work(self):
        if self.car.drive():
            logging.info("Поїхав на роботу")

            self.money += self.job.salary
            self.gladness -= self.job.gladness_less
            self.safety -= 4

            logging.info(
                f"Заробив {self.job.salary}. "
                f"Баланс: {self.money}"
            )

        else:
            if self.car.fuel < 20:
                logging.warning("Мало палива")
                self.shopping("fuel")
                return
            else:
                logging.warning("Ремонт авто")
                self.to_repair()
                return

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
            logging.info("Куплено паливо")

            self.money -= 100
            self.car.fuel += 100

        elif manage == "food":
            print("Купуємо продукт...")
            logging.info("Куплено продукти")

            self.money -= 50
            self.home.food += 50

        elif manage == "delicacies":
            print("Купуємо делікатеси...")
            logging.info("Куплено делікатеси")

            self.money -= 15
            self.gladness += 10
            self.safety += 2

    def chill(self):
        logging.info("Відпочиває")

        self.gladness += 10
        self.home.mess += 5

    def clean_home(self):
        logging.info("Прибирає будинок")

        self.gladness -= 5
        self.home.mess = 0

    def to_repair(self):
        logging.warning("Ремонт авто")

        self.car.strength += 100
        self.money -= 50

    def walk_with_pet(self):
        logging.info("Прогулянка з собакою")

        self.pet.walk()
        self.is_pet_want_to_eat()

    def is_pet_want_to_eat(self):
        if self.pet.want_to_eat():
            self.pet.eat()
            self.money -= 20

            logging.info("Нагодував собаку")

    def go_to_pet_doctor(self):
        logging.warning("Візит до ветеринара")

        self.pet.visit_doctor()
        self.money -= 40
        self.gladness -= 10

    def need_a_pet_doctor(self):
        if self.pet.need_a_doctor():
            self.go_to_pet_doctor()
        else:
            print("Цуцик у порядку")

    def days_index(self, day):

        logging.info(f"------ День {day} ------")

        print(f"{' День ' + str(day):=^50}")

        print(f"Money - {self.money}")
        print(f"Satiety - {self.safety}")
        print(f"Gladness - {self.gladness}")

        print(f"Food - {self.home.food}")
        print(f"Mess - {self.home.mess}")

        print(f"Fuel - {self.car.fuel}")
        print(f"Strength - {self.car.strength}")

        print(f"Pet health - {self.pet.health}")
        print(f"Pet satiety - {self.pet.satiety}")

    def is_alive(self):

        if self.gladness < 0:
            print("Depression...")
            logging.error("Депресія")
            return False

        if self.safety < 0:
            print("Dead...")
            logging.error("Смерть")
            return False

        if self.money < -500:
            print("Bankrupt...")
            logging.error("Банкрутство")
            return False

    def live(self, day):

        if self.is_alive() == False:
            return False

        if self.home is None:
            self.get_home()

        if self.car is None:
            self.get_car()

        if self.job is None:
            self.get_job()

        if self.pet is None:
            self.get_pet()

        self.days_index(day)

        dice = random.randint(1, 4)

        if self.safety < 20:
            self.eat()

        elif self.gladness < 20:

            if self.home.mess > 15:
                self.clean_home()
            else:
                self.chill()

        elif self.money < 0:
            self.work()

        elif self.car.strength < 15:
            self.to_repair()

        elif dice == 1:
            self.chill()

        elif dice == 2:
            self.work()

        elif dice == 3:
            self.clean_home()

        elif dice == 4:
            self.shopping("delicacies")

        self.walk_with_pet()
        self.need_a_pet_doctor()


class Auto:

    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.fuel = brand_list[self.brand]["fuel"]
        self.strength = brand_list[self.brand]["strength"]
        self.consumption = brand_list[self.brand]["consumption"]

    def drive(self):

        if self.strength > 0 and self.fuel >= self.consumption:

            self.fuel -= self.consumption
            self.strength -= 1

            return True

        else:
            logging.warning("Авто не може їхати")
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
        logging.info("Собака їсть")

        self.satiety += 10

    def visit_doctor(self):

        print("Собака у лікаря")
        logging.warning("Собака у лікаря")

        self.health = 50
        self.satiety = 50

    def walk(self):

        print("Собака гуляє")
        logging.info("Собака гуляє")

        self.satiety -= 10

        with_trauma = random.randint(0, 1)

        if with_trauma == 1:
            print("Собака травмувалась")
            logging.warning("Собака травмувалась")

            self.health -= 10

        else:
            self.health -= 1


job_list = {
    "Java developer": {"salary": 50, "gladness_less": 10},
    "Python developer": {"salary": 40, "gladness_less": 3},
    "C++ developer": {"salary": 45, "gladness_less": 25},
    "Rust developer": {"salary": 70, "gladness_less": 1},
}

brands_of_car = {
    "BMW": {"fuel": 100, "strength": 100, "consumption": 6},
    "Lada": {"fuel": 50, "strength": 40, "consumption": 10},
    "Volvo": {"fuel": 70, "strength": 150, "consumption": 8},
    "Ferrari": {"fuel": 80, "strength": 120, "consumption": 14},
}

names_of_pet = ["Чак", "Артемон", "Бурулька", "Шарик"]

random_index = random.randint(0, 3)
name_of_pet = names_of_pet[random_index]


class Job:

    def __init__(self, job_list):

        self.job = random.choice(list(job_list))

        self.salary = job_list[self.job]["salary"]

        self.gladness_less = job_list[self.job]["gladness_less"]


nick = Human(name="Nick")

for day in range(1, 8):

    if nick.live(day) == False:
        break

logging.info("Програма завершена")