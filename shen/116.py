a, b = int(input()), int(input())
c = 0
x,y = 0, 0
while x < a and y < b:
    x += 1
    y += 1
    c += 2
while x < a:
    x += 1
    c +=1
while y < b:
    y += 1
    c += 1

print(int(c))