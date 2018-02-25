"""Перемножение матриц"""

''' такой способ создания многомерно массива неправильный: z = [[0]*2]*2 так как создаст один список на который ссылаются две переменные. то есть находиться он будет на одном и том же адресе '''
""""Ищет n число Фибоначчи путем возведения матрицы в степень"""

def mult_m(a,b):
    la = len(a)
    lb = len(b)
    la0 = len(a[0])
    lb0 = len(b[0])
    c = []
    k = len(a[0])

    if (len(a) and len(b)) != 0:
        if len(a[0]) == lb:
            for x in range(len(a)):
                c.append([])
                for y in range(len(a[0])):
                    sum1 = 0
                    for z in range(k):
                        sum1 += a[x][z]*b[z][y]
                    c[x].append(sum1)
                    #print(c)
    return c


def fib(n):
    print("You find {} number of Fibonacci ".format(n))
    c = [[1,1],[1,0]]
    a = [[1,1],[1,0]]
    while n > 1:
        print('before',a)
        a  = mult_m(a, c)
        print('after',a)
        n -= 1
    return a


def _main():

    answ = fib(7)[1][1]
    print(str(answ))

if __name__ == "__main__":
    _main()





