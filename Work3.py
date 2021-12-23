import random 

def generateRandomSeq():
    randomSeq = []
    f = True
    while len(randomSeq) < 4:
        r = random.randint(0,9)
        for j in randomSeq:
            if r == j:
                f = False
        if f:
            randomSeq.append(r)
        f = True

    return randomSeq

def Game(randomSeq):
    c = 0
    b = 0
    while b != 4:
        b = c = 0
        str = (input('Введите число'))
        if str == '-1':
            break
        A = list(str)
        for x in range(len(randomSeq)):
            if randomSeq[x] == int(A[x]):
                b += 1
        for i in range(len(randomSeq)):
            for j in range(len(A)):
                if randomSeq[i] == int(A[j]):
                    c += 1
        print('Быки - ', b)
        print('Коровы - ',c)


randomSeq = generateRandomSeq()
print(randomSeq)
Game(randomSeq)