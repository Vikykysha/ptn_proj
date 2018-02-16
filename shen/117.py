import math
a, b = int(input()), int(input())

k = 1
if (b > a) :
    k = 0
else:
    while k * b < a:
        k += 1

div = k
mod = a - k * b

l = divmod(3,4)
print(l)
print(str(div), str(mod), sep=',')

