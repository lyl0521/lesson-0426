# 打印出所有的“水仙花数”，所谓“水仙花数”是指一个三位数，其各位数字立方和等于该数本身。例如：153是一个“水仙花数’，因为153=1 的三次方＋5的三次方＋3的三次方

counter = 0

for i in range(100,1000):
    a = int(i % 10)
    b = int(i / 100 % 10)
    c = int(i / 10 % 10)
    num = a*a*a+b*b*b+c*c*c
    if num == i:
        print(str(i)+'是水仙花数')