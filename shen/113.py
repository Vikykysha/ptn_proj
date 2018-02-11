"""Степень без рекурсии"""

a, n = int(input()), int(input())

#Вариант за O(n)
'''b = 1
for _ in range(n):
    b *= a

print(b)'''

#Вариант за O(logn)
k = a
while n > 1:
    if n % 2 == 0:
        a *= a
        n = n / 2
    else:
        a = a * k
        n = n - 1
print(a)