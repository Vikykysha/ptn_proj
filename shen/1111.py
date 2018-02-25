def garm(n):
    sum = 0
    track = 1
    mult = 1
    while n > 0:
        if sum == 0:
            sum = 1
            n -= 1
        else:
            track = track * mult
            print(track)
            sum = sum + 1 / track
            mult += 1
            n -= 1
    return sum

i = int(input("Введите номер числа гармонического ряда: "))
print(garm(i))


# Вариант через n операций присваивания

def garm1(n):
    sum = 0
    last = 1
    for i in range(1, n + 1):
        sum += last
        last = last * 1 / i
    return sum

print(garm1(int(input("Введите n для подсета значений гармонического ряда через второй алгоритм: "))))

