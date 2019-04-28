score = 70
if score > 60:
    print('pass')

    if score > 60:
        print('pass')
    else:
        print('failed')

if score > 90:
    print('a')
elif score > 80:
    print('b')
else:
    print('c')

    print(' ' * 3, end='')
    print('x')
    print(' ' * 2, end='')
    print('x' * 3)
    print(' ', end='')
    print('x' * 5)
    print('x' * 7)
    print(' ', end='')
    print('x' * 5)
    print(' ' * 2, end='')
    print('x' * 3)
    print(' ' * 3, end='')
    print('x')

    for i in range(1, 10, 1):
        if i % 2 == 0:
            print(i, '是偶数')
        else:
            print(i, "是奇数")

    is_found = False
    fruits = ['apple', 'banana', 'orange']
    for fruit in fruits:
        print(fruit)
        if fruit == 'watermelon':
            print('found watermelon')
            # is_found = True
            break
    else:
        print('not found watermelon')
# if is_found == False:  # 方法二
#     print('not found watermelon')

 # 判断101-200之间有多少个素数，并输出所有素数。
# 素数：只能被1和它本身整除的正整数（1不是素数）

    count = 0
    for i in range(101,201):
        for j in range(2,i):
            if i % j == 0:
                print(i,'不是素数')
                break
        else:
            print(i,'是素数')
            count += 1
    print(count)

    rows = 5
    for i in range(rows):
        for j in range(rows-i-1):
            print(' ',end='')
        for k in range(2*i-1):
            print('x',end='')
        print('')
    rows = 4
    for i in range(1,rows):
        for j in range(i):
            print(' ',end='')
        for k in range(2 * ( rows - i ) - 1):
            print('x',end='')
        print('')





