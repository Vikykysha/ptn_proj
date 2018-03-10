

def gcd1(a, b):
    if a >= b:  
        if a %  b == 0:
            return b
        return gcd1(b, a % b)
    else:
        if b %  a == 0:
            return a
        return gcd1(a, b % a)

def find_d_expr(a,b,d,inequl):
    if a == d:
        x = 1
        y = 0
        return x,y
    elif b == d:
        x = 0
        y = 1
        return x, y
    if inequl:
        x = 1
        y = - (a // d - b // d -1)
        return x,y
    else:
        y = 1
        x = - (b // d - a // d - 1)
        return x,y



a,b = int(input()), int(input())

a_big = a > b
d = gcd1(a,b)
print(str(d))
print(str(find_d_expr(a,b,d,a_big)))