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

                

print(gcd(6,336))
             