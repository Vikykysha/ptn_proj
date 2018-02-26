#GCD

# Метод грубой силы

def gcd(a, b):
    if a > b:
        gcd_ = 1
        for i in range (1, b + 1):
            if a % i == 0 and b % i == 0:
                if i > gcd_:
                    gcd_ = i
    else:
        gcd_ = 1
        for i in range (1, a + 1):
            if a % i == 0 and b % i == 0:
                if i > gcd_:
                    gcd_ = i
    return gcd_
                
#Алгоритм Евклида

def gcd1(a, b):
    if a >= b:  
        if a %  b == 0:
            return b
        return gcd1(b, a % b)
    else:
        if b %  a == 0:
            return a
        return gcd1(a, b % a)

print(gcd1(9,24))

#Другой вариант Евклида

def gcd2(a, b):
    m = a 
    n = b
    while m > 0 or n > 0:
        if m > n:
            m -= n
        else:
            n -= m
    if m == 0:
        return n
    else:
        return m
             