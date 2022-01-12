from abc import ABC, abstractclassmethod

class Product(ABC):
    def __init__(self, title, count):
        super().__init__()
        self.__title = title
        self.__count = count

    @abstractclassmethod
    def calculate_price():
        pass

    def calculate_final_cost(self):
        return self.calculate_price() * self.count

    @property
    def title(self):
        return self.__title


    @property
    def count(self):
        return self.__count

    @title.setter
    def title(self, title):
        self.__title = title

   
    @count.setter
    def title(self, count):
        self.__count = count

    def show(self):
        print(f'Итоговая стоимость {self.title} - {self.calculate_final_cost()}')

    
class Digital(Product):
    def __init__(self, title, price, count):
        super().__init__(title, count)
        self.price = price

    def calculate_price(self):
        return self.price


class Real(Product):
    def __init__(self, title, count, price):
        super().__init__(title, count)
        self.price = price

    def calculate_price(self):
        return  self.price * 2    

class Weight(Product):
    def __init__(self, title, count, weight, cost_kilo):
        super().__init__(title, count)
        self.weight = weight
        self.cost_killo = cost_kilo

    def calculate_price(self):
        return self.weight * self.cost_killo * self.count


digital = Digital('Macbook', 100000, 30)
real = Real('Macbook', 20, digital.price)
wieght = Weight('Macbook', 10, 1.2, 70000)

digital.show()
real.show()
wieght.show()




    