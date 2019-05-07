def fn_recursive(n):
    if n == 1:
        return 1
    else:
        return n * fn_recursive(n - 1)


print(fn_recursive(10))


def fn_fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fn_fibonacci(n - 1) + fn_fibonacci(n - 2)


print(fn_fibonacci(10))


def square(x):
    return x**2

print(list(map(square,[1,2,3,4,5])))

print(list(map(lambda x: x**2 ,[1,2,3,4,5])))