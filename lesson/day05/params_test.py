def power(x):
    return x*x


print(power(2))


def power(x,n=3):
    p = 1
    while n>0:
        p *= x
        n -= 1
    return p


print(power(3))


def fn_append(array=None):
    if array is None:
        array = []
    array.append('END')
    return array


print(fn_append([1,2,3]))

print(fn_append())
print(fn_append())

print(max(1,2,3,4))


def fn_sum(*numbers):
    print(numbers)
    s = 0
    for n in numbers:
        s += n
    return s


# print(fn_sum(1,2,3,4,5))

num = (1,2,3,4,5)
print(fn_sum(num[0],num[1],num[2],num[3],num[4]))
print(fn_sum(*num))