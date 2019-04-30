# 输入三个整数x，y，z，请把这三个数由小到大输出。

x,y,z = map(int,input('请输入三个整数').split(' '))

arr = []
arr.append(x)
arr.append(y)
arr.append(z)

for i in range(len(arr)):
    for j in range(len(arr)):
        if arr[j]>arr[i]:
            temp = arr[j]
            arr[j] = arr[i]
            arr[i] = temp
for i in range(len(arr)):
    print(arr[i],end=' ')
