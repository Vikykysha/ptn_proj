a,b = int(input()), int(input())


m = a
n = b
p = 1
q = 0
r = 0
s = 1

while not (m == 0 or n == 0):
    if m >= n:
         m -= n
         p -= r
         q -= s
    else:
        n -= m
        r -= p
        s -= q
if m == 0:
    k = n
    x = r
    y = s
else:
    k = m
    x = p
    y = q

print('gcd = ', k, 'ost = ' ,x,y)