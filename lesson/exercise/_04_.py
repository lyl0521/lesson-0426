# 将一个正整数分解质因数。例如：输入90，打印出90=2*3*3*5。


from math import sqrt

num = int(input('请输入一个正整数'))
res = num
arr = []
while 1:
        for i in range(2,int(sqrt(num)+1)):
            if num % i == 0:
                arr.append(i)
                num=int(num/i)
                break
        else:
            arr.append(num)
            break

print((str(num)+'='+str(arr[0])),end='')
for i in range(1,len(arr)):
    print(('*'+str(arr[i])),end='')