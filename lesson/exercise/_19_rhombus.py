# 打印菱形

rows = 5
for i in range(rows):
    for j in range(rows - i - 1):
        print(' ', end='')
    for k in range(2 * i - 1):
        print('x', end='')
    print('')
rows = 4
for i in range(1, rows):
    for j in range(i):
        print(' ', end='')
    for k in range(2 * (rows - i) - 1):
        print('x', end='')
    print('')


print('')


s = '*'
for i in range(1, 8, 2):
    print(('x'*i).center(7))
for i in reversed(range(1,6,2)):
    print(('x'*i).center(7))


rows = int(input('请输入需要的行数：'))
for i in range(1,rows,2):
    t = (rows-1-i)//2
    print(' '*t + 'x'*i + ' '*t)
for i in reversed(range(1,rows-2,2)):
    t = (rows-1-i)//2
    print(' '*t + 'x'*i + ' '*t)

name=[]

