# 杨辉三角
n = int(input('请输入需要的行数n：'))


def parsc(i,j):
    if j == 0 or i == j:
        return 1
    else:
        return parsc(i-1,j-1)+parsc(i-1,j)



for i in range(0,n):
    for k in range(0,10-i):
        print(' ',end='')
    for j in range(0,i+1):
        print(parsc(i,j),end=' ')
    print()
