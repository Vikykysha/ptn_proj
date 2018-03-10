
c = [int(i) for i in input().split(' ')]



for i in range(c[0], c[1] + 1):
    if i % 15 == 0:
        print('FizzBuzz')
    elif i % 5 == 0:
        print('Buzz')
    elif i % 3 == 0:
        print('Fizz')
    else:
        print(str(i))