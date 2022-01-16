import random
from Car import *


class Factory:
    def __init__(self, title_factory):
        self.title_factory = title_factory

    def create_car(self, title_car):
        print(f"Завод {self.title_factory} начинает сборку автомобиля {title_car}...")
        car = Car(title_car,random.randint(1000,5000))
        return car