matrix = [
    [2,3,4],
    [5,6,7],
    [3,2,6]
]

matrixNew = [
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0]
]

# 1) Сохранить матрицу в файле
# 2) Считыаем матрицу из файла и выводим в консоль элементы матрицы таким образом, чтобы каждый элемент был возведен в степень
# равную номеру строки, в которой он находится



file = open('matrix1.txt','w')
i = 0
while i < len(matrix):
    j = 0
    s = ''
    while j < len(matrix[i]):
        s += str(matrix[i][j]) + ' '
        j += 1
    file.write(s + '\n')
    i += 1
file.close()

with open('matrix1.txt','r') as file:
    i = 0
    j = 0
    for line in file:
        i += 1
        mas = line.split(' ')
        for item in mas:
            if item != '\n':
                print(int(item) ** i,end=' ')
                matrixNew[i-1][j] = int(item)
                matrixNew[i-1][3] += int(item)
                matrixNew[3][j] += int(item)
                matrixNew[3][3] += int(item)
                j += 1
        j = 0
        print()

print(matrixNew)

with open('matrix1.txt', 'a') as file:
    file.write('\n')
    i = 0
    while i < len(matrixNew):
        j = 0
        s = ''
        while j < len(matrixNew[i]):
            s += str(matrixNew[i][j]) + ' '
            j += 1
        file.write(s + '\n')
        i += 1

# 2) Сделать отдельный столец и строку, где вычисляем сумму по строкам и столбцам

