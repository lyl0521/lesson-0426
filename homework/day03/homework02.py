# 求一个数值List的最大/最小元素值

arr = [25,3,6,4,26,8,16,38,59]
min = 0
max = 0

for i in range(len(arr)):
    for j in range(0,i):
        if arr[j] > arr[i]:
            temp = arr[j]
            arr[j] = arr[i]
            arr[i] = temp

print(arr)
print('最大值为',arr[-1])
print('最小值为',arr[0])
