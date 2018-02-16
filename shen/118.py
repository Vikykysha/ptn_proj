n = int(input())
k = n

if n == 0:
    n = 1
else: 
    while k >1:
        print(str(k), end= ',')
        k -= 1
        n *= k
        
print(str(n))