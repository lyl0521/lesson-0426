# 输入两个正整数m和n，
# 求其最大公约数和最小公倍数。

a = int(input('请输入第一个数字：'))
b = int(input('请输入第二个数字：'))


def gys(a, b):
    if a > b:
        small = b
    else:
        small = a
    for i in range(small, 0, -1):
        if a % i == 0 and b % i == 0:
            return i


num = gys(a,b)
gbs =  int((a*b)/num)

print('最小公倍数为：'+ str(gbs))
print('最大公约数为：'+ str(gys(a,b)))