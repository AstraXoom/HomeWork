import math
import random

#Задание 1: Вывести на экран все целые числа от 100 до 200 кратные 3 и посчитать сумму этих цифр
N = 100
sum = 0
while N <= 200:
    if N % 3 == 0:
        sum = sum + N
        print(N)
    N += 1
print ('sum - ', sum)

#Задание 2: Вывести на экран все простые числа от 2 до 100
num = 2
flag = True
while num <= 100:
    a = 2
    while a <= math.floor(math.sqrt(num)):
        if (num % a == 0):
            flag = False
            break
        a += 1
    if flag:
        print(num)
    num += 1
    flag = True

#Сделать игру “Казино”. У игрока есть исходная сумма средств. Если сумма от 1000р., 
# то игрок допускается к игре. Загадывается случайное число от 1 до 10 и за 3 попытки 
# игрок должен его угадать. Перед началом игры игрок делает ставку на какое-либо число. 
# Если он угадывает за 3 попытки, его ставка увеличивается вдвое, а если не угадывает, 
# ставка сгорает. Игрок может в любое время завершить игру введя вместо ответа STOP. 
# Игра по умолчанию продолжается пока у игрока не закончатся средства.


money = int(input('Положите деньги в казино (минимальная сумма 1000) - '))
if money < 1000:
    print('сумма < 1000. Вход в казино закрыт')
else:
    print('Операция прошла успешно! Ваш счет - ', money)

    while money >= 1000:
        bet = int(input('Введите вашу ставку - '))

        if bet == 0:
            print('Возвращайтесь еще! На ваш счет было зачисленно - ', money)
            break


        if bet > money:
            print('Ставка не может быть больше чем сумма на вашем счету')
            continue

        print('Ставка успешно принята!')

        RandomNumber = random.randint(1,10)
        count = 3

        while count > 0:
            UserRandomNumber = input('Какое число от 1 до 10 мы загадали? - ')

            if UserRandomNumber == 'WIN':
                #чит режим(не относится к заданию) 
                #позволяет нам узнавать какое число было загадано и всегда побежать
                print('...мы думаем это число - ', RandomNumber, ' ...')
                continue

            if UserRandomNumber == 'STOP':
                print('Возвращайтесь еще!')
                break

            if int(UserRandomNumber) == RandomNumber:
                print('Поздравляем, Вы угадали! Ваша ставка удвоена')
                print('Сумма в банке - ', money + bet * 2)
                break
            else:
                count -= 1
                print('Вы не угадали. Попробуйте снова. Кол-во попыток - ', count)
                
        if count == 0:
            print('Вы проиграли, попробуйте снова')
            money = money - bet
