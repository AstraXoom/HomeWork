from abc import ABC, abstractclassmethod

class Employee(ABC):
    def __init__(self, rate):
        super().__init__()
        self.rate = rate
    
    @abstractclassmethod
    def calculate_salary():
        pass

class Programmer(Employee):
    def calculate_salary(self):
        return self.rate * 4

class Economist(Employee):
    def calculate_salary(self):
        return self.rate * 2

class Director(Employee):
    def calculate_salary(self):
        return self.rate * 10

programmer = Programmer(10000)
economist = Economist(10000)
director = Director(100000)

print('programmer - ', programmer.calculate_salary())
print('economist - ', economist.calculate_salary())
print('director - ', director.calculate_salary())