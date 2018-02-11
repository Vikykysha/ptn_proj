"""Обменяй значения переменных, не используя дополнительную переменную"""
def cng(a,b):
    a = a + b
    b = a - b
    a = a - b
    return a, b

x,y = int(input()), int(input())
print("Your old value of x is " + str(x) + ", of y is " + str(y)) 
x, y = cng(x,y)
print("After change your value of x is " + str(x) + ", of y is " + str(y))