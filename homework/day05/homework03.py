# 斐波那契数列


def fn_fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fn_fibonacci(n - 1) + fn_fibonacci(n - 2)


n = int(input('请输出需要的位数n:'))
print(fn_fibonacci(n))
