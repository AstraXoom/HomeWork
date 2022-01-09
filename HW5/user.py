import json

def isExist(filePath, comparedElement):
    with open(filePath,'r') as file:
        users = json.load(file)
        for x in users['users']:
            if comparedElement == x['userID']:
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

def loadInFile(filePath, text):
    with open(filePath, 'r') as file:
        temp = json.load(file)
        temp['users'].append(text)
    with open(filePath, 'w') as file:
        json.dump(temp, file, indent=4)

    


def addUser(filePath):
    newUser = ''
    while True:
        newUser = input('Введите идентификатор пользователя - ')
        if len(newUser) <= 1:
            print('Имя слишком короткое')
            continue
        if isExist(filePath, newUser):
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
        loadInFile(filePath, {"userID": newUser, "userPass": password})
    


def changePass(filePath):
    userLogin = input('Введите идентификатор пользователя - ')
    if isExist(filePath, userLogin):
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
            with open(filePath, 'r') as file:
                temp = json.load(file)
                for i in temp['users']:
                    if i['userID'] == userLogin:
                        i['userPass'] = newPass
                        break
            
            with open(filePath, 'w') as file:
                json.dump(temp,file, indent=4)
    else:
        print('Пользователь не найден')      

def showUsers(filePath):
    with open(filePath,'r') as file:
        users = json.load(file)
        for x in users['users']:
            print(x['userID'])

userInput = 0
filePath = 'userPass.json'

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
        addUser(filePath)
    if userInput == 2:
        changePass(filePath)
    if userInput == 3:
        showUsers(filePath)