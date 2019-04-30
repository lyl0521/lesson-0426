# 一个数如果恰好等于它的因子之和，这个数就称为’完数’。
# 例如6=1＋2+3.编程 找出1000以内的所有完数

for i in range(2,1001):
    arr = []
    n = -1    #  计算数组下标
    s = i
    for j in range(1,i):
        if i % j == 0:      #  判断是否为因数
            n += 1          #  如果是因数，数组下标+1
            s -= j          #  计算减去因数后 i 的大小
            arr.append(j)   #  将因数加入数组

    if s == 0:              #  如果因数相加刚好等于i 继续
        print(i,end='=')    #  输出符合要求的数
        for k in range(n):  #  循环输出改数对应的因数
            print(str(arr[k]),end='+')
        print(arr[n])       #  因为循环次数为n-1 不能全部输出，
        # 最后一个因数直接输出数组中的最后一个arr[n]