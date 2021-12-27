import csv

def loadFile(path, mode):

    try:
        return open(path, mode, encoding='utf8')
    except Exception as massage:
        print('Ошибка - ', massage)
        return False


def chekProduct( userProduct, product ):
    for row in product:
        if userProduct in row:
            return True
    return False

def showProduct(filePath):
    file = loadFile(filePath, 'r')
    reader = csv.reader(file)
    for row in reader:
        print(row)
    file.close()

def addProduct(filePath):
    file = loadFile(filePath, 'r+')
    reader = csv.reader(file)
    name = input('Введите название товара - ')
    cost = input('Введите стоимость товара - ')
    disc = input('Введите описание товара - ')
    str = name + ',' + cost + ',' + disc + '\n'
    if not chekProduct(name, reader):
        file.write(str)
    else:
        print('Такой товар уже существует')
    file.close()

def deleteProduct(filePath):
    file = loadFile(filePath, 'r')
    delete = input('Введите название товара - ')
    reader = list(csv.reader(file))
    file.close()
    file = loadFile(filePath, 'w')
    for row in reader:
        if delete  != row[0]:
            file.write(','.join(row) + '\n')
    file.close()

def searchProduct(filePath):
    file = loadFile(filePath, 'r')
    search = input('Введите название товара - ')
    reader = list(csv.reader(file))
    flag = True
    for row in reader:
        if search == row[0]:
            print(row)
            flag = False
            break
    if flag:
        print('Товар не найден')


userInput = ''
filePath = input('Введите путь до файла - ')
load = loadFile(filePath, 'r')

while userInput.upper() != 'EXIT' and load:

    print('''
        LIST - отобразить товары
        ADD - добавить товар
        DELETE - удалить товар
        SEARCH - поиск по каталогу
        EXIT - выход
    ''')
    userInput = input('Выберите действие - ')

    if userInput.upper() == 'LIST':
        showProduct(filePath)

    if userInput.upper() == 'ADD':
        addProduct(filePath)
    
    if userInput.upper() == 'DELETE':
        deleteProduct(filePath)

    if userInput.upper() == 'SEARCH':
        searchProduct(filePath)