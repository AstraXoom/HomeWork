import pymysql

connect = pymysql.connect(host='localhost',
                          user='root',
                          password='root',
                          db='users_passwords',
                          cursorclass=pymysql.cursors.DictCursor
                        )
def isExist(comparedElement):
    cur = connect.cursor()
    cur.execute(f'SELECT UserName FROM `users_pass` WHERE UserName = \'{comparedElement}\'')
    connect.commit()
    rows = cur.fetchall()
    cur.close()
    if rows:
        return True
    return False

def verificationPassword(password):
    strong = 0
    alphaUpper = 0
    alphaLower = 0
    passDigit = 0
    passMark = 0
    if len(password) > 8:
        strong += 1
    for i in password:
        if i.isdigit() and passDigit == 0:
            passDigit += 1
            strong += 1
        elif (i in '!$%&£') and passMark == 0:
            passMark += 1
            strong += 1
        elif i.isupper() and alphaUpper == 0:
            alphaUpper += 1
            strong += 1
        elif not i.isupper() and  alphaLower == 0:
            alphaLower += 1
            strong += 1

    return strong

def addUser():
    newUser = ''
    while True:
        newUser = input('Введите идентификатор пользователя - ')
        if len(newUser) <= 1:
            print('Имя слишком короткое')
            continue
        if isExist(newUser):
            print('Такой идентификатор пользователя уже существует, попробуйте снова')
            continue
        break
    while True:
        password = input('Введите пароль - ')
        strong = verificationPassword(password)
        if strong <= 2:
            print('Пароль откланен. Слишком слабый пароль')
            break
        elif strong == 3 or strong == 4:
            upPass = input('Пароль можно улучшить хотите повторить попытку?(Y/N)')
            if upPass.upper() == 'Y':
                continue
            else:
                print('Пользовтель успешно создан!')
                break
        if strong == 5:
            print('Пользователь успешно создан!')
            break
    if strong >= 3:
        cur = connect.cursor()
        cur.execute(f'INSERT INTO `users_pass` (UserName, UserPass) VALUES (\'{newUser}\', \'{password}\')')
        connect.commit()
        cur.close()

def changePass():
    userLogin = input('Введите идентификатор пользователя - ')
    if isExist(userLogin):
        while True:
            newPass = input('Введите пароль - ')
            strong = verificationPassword(newPass)
            if strong <= 2:
                print('Пароль откланен. Слишком слабый пароль')
                break
            elif strong == 3 or strong == 4:
                upPass = input('Пароль можно улучшить хотите повторить попытку?(Y/N)')
                if upPass.upper() == 'Y':
                    continue
                else:
                    print('Пароль успешно изменен!')
                    break
            if strong == 5:
                print('Пароль успешно изменен!')
            break
        if strong >= 3:
            cur.execute(f'UPDATE `users_pass` SET UserPass = \'{newPass}\' WHERE UserName = \'{userLogin}\'')
            connect.commit()
            cur.close()
    else:
        print('Пользователь не найден')      

def showUsers():
    cur.execute('select username from users_pass')
    connect.commit()
    rows = cur.fetchall()
    cur.close()
    for name in rows:
        print(name['username'])

userInput = 0
with connect:
    cur = connect.cursor()
    while userInput != 4:
        print(
            '''
            1) Добавить пользователя
            2) Изменить пароль
            3) Вывести пользователей
            4) Выход
            '''
        )
        try:
            userInput = int(input('Введите номер операции - '))
        except Exception as massage:
            print(massage)
            continue
        if userInput == 1:
            addUser()
        if userInput == 2:
           changePass()
        if userInput == 3:
            showUsers()