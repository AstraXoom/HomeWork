import random
from Order import *


def f():
    marki = ["Audi","Skoda","VW","Porshe"]
    dealer = Dealer('Fresh Auto', 'Да')
    order = Order("VAG",marki, 10, dealer)

if __name__ == '__main__':
    f()