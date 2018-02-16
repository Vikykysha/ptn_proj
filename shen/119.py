n = int(input())
a = 0
b = 1
c = 0
while n > 1:
    c = a + b
    a, b =b, c
    n -= 1
print(str(c))

