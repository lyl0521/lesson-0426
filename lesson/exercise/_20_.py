# 有一分数序列：2 / 1，3 / 2，5 / 3，8 / 5，13 / 8，21 / 13…求出这个数列的前20项之和。

n1 = 1
n2 = 1
count = 0
arr = []
#   分子部分数列
for i in range(1, 21):
        count = n1 + n2
        arr.append(count)
        n1 = n2
        n2 = count

print(arr)

x1 = 1
x2 = 1
number = 0
arr1 = []
#   分母部分数列
for i in range(2, 22):
    if i == 2:
        arr1.append(1)
    else:
        number = x1 + x2
        arr1.append(number)
        x1 = x2
        x2 = number

print(arr1)

sum = 0
for i in range(0,20):
    sum += int(arr[i])/int(arr1[i])

print(sum)