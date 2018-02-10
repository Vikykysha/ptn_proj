import sys

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

deg = b ** 2 - 4 * a *c

x1 = (-b + deg ** 0.5) / 2 * a
x2 = (-b - deg ** 0.5) / 2 * a

print(int(x1),  int(x2), sep='\n')
