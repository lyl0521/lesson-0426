# 斐波那契数列
# 古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，
# 假如兔子都不死，问每个月的兔子总数为多少？

n1 = 1
n2 = 1
count = 0

for i in range(1, 100):
    if i == 1:
        print(1)
    elif i == 2:
        print(1)
    else:
        count = n1 + n2
        print(count)
        n1 = n2
        n2 = count
