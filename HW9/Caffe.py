class Burger:
    def __init__(self, size, filling, additionally):
        self.size = size
        self.filling = filling
        self.additionally = additionally
    
    def count_calories(self):
        return self.size.calories + self.filling.calories + self.additionally.calories

    def count_price(self):
        return self.size.price + self.filling.price + self.additionally.price

class Config:
    def __init__(self, name, price, calories):
        self.__name = name
        self.__price = price
        self.__calories = calories

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    @property
    def calories(self):
        return self.__calories

class Builder_burger:
    def __init__(self):
        self.size = None
        self.filling = None
        self.additionally = None
        self.burger = Burger(self.size, self.filling, self.additionally)

    def set_size_small(self):
        self.size = Config('Маленький',50,20)
    
    def set_size_big(self):
        self.size =  Config('Большой',100,40)

    def set_filling_cheese(self):
        self.filling = Config('Сыр',10,20)
    
    def set_filling_salad(self):
        self.filling = Config('Салат',20,5)

    def set_filling_potato(self):
        self.filling = Config('Картошка',15,10)

    def set_additionally_seasoning(self):
        self.additionally = Config('Приправа',15,0)

    def set_additionally_sauce(self):
        self.additionally = Config('Майонез',20,5)

    def count_calories_builder(self):
        self.burger = Burger(self.size, self.filling, self.additionally)
        return self.burger.count_calories()

    def count_price_builder(self):
        self.burger = Burger(self.size, self.filling, self.additionally)
        return self.burger.count_price()


builder = Builder_burger()
builder.set_size_big()
builder.set_filling_cheese()
builder.set_additionally_seasoning()
print(builder.count_calories_builder())
print(builder.count_price_builder())






    

