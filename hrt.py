grid=[['.','.','.','.','.','.'],
['.','0','0','.','.','.'],
['0','0','0','0','.','.'],
['0','0','0','0','0','.'],
['.','0','0','0','0','0'],
['0','0','0','0','0','.'],
['0','0','0','0','.','.'],
['.','0','0','.','.','.'],
['.','.','.','.','.','.']]


x=len(grid[0])
y=len(grid)
for i in range(x):
    for j in range(y):
        print(grid[j][i],end='')
    print('\n')
