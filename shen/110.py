"""Перемножение матриц"""

''' такой способ создания многомерно массива неправильный: z = [[0]*2]*2 так как создаст один список на который ссылаются две переменные. то есть находиться он будет на одном и том же адресе '''

def mult_m(a,b):
    la = len(a)
    lb = len(b)
    la0 = len(a[0])
    lb0 = len(b[0])
    c = []
    print(c)
    k = len(a[0])
    print('la=' +str(la) +'lb='+ str(lb))
    if (len(a) and len(b)) != 0:
        if len(a[0]) == lb:
            for x in range(len(a)):
                c.append([])
                for y in range(len(a[0])):
                    sum1 = 0
                    for z in range(k):
                        sum1 += a[x][z]*b[z][x]
                    c[x].append(sum1)
                    print(c)
    return c


def _main():
    a = [[12,1],[1,1]]
    b = [[2,2],[2,2]]
    k = mult_m(a,b)
    print(k)
if __name__ == "__main__":
    _main()





