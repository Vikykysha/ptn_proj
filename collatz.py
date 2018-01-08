def collatz(number):
    if number % 2 == 0:
         return number/2
    else:
         return 3*number-1

print("Enter a number, please")

try:

    num=int(input())
    while num != 1:
        num = collatz(num)
        print(int(num), end='\n')
except ValueError:
    print('Please, enter a NUMBER!')
