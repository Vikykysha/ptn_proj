from __future__ import print_function
def l(lst):
    count =  len(lst) - 1

    for i in lst:
        if count == 0:
            print('and ' + str(i), end=' ')
        else:
            print(str(i),end=', ')
        count = count-1
