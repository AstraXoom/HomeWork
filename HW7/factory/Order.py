import random

from Factory import *
from Dealer import *

class Order:
    def __init__(self, title_factory, marki, count_cars, dealer):
        self.title_factory = title_factory
        self.cars = []
        self.price_order = 0
        self.dealer = dealer
        self.create_order(count_cars, marki)
        self.count = {}
        self.count_marks(self.cars, marki)
        self.show()

    def show(self):
        print(f"Информация о заказе:\n")
        for car in self.cars:
            print(f"Автомобиль {car.name} стоит {car.price}. Автосалон - {self.dealer.name}, Тест-драйв - {self.dealer.testDrive}\n")
        print(f"Сумма заказа: {self.price_order}")
        print(self.count)
        

    def create_order(self,count_cars, marki):
        factory = Factory(self.title_factory)
        for i in range(0,count_cars):
            car = factory.create_car(marki[random.randint(0,len(marki) - 1)])
            self.cars.append(car)
            self.price_order += car.price

    def count_marks(self, cars, marki):
        self.count = dict.fromkeys(marki, 0)
        for car in self.cars:
            for key in self.count:
                if car.name == key:
                    self.count[key] += 1

