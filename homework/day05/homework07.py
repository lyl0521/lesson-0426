# mao
from filecmp import cmp


def square(x):
    return x ** 2


# map()的返回值已经不再是list,而是iterators, 所以想要使用，

# 只用将iterator 转换成list 即可，比如 list(map())

print(list(map(square, [1, 2, 3, 4, 5])))

print(list(map(lambda x: x ** 2, [1, 2, 3, 4, 5])))

print(list(map(lambda x, y: x + y, [1, 3, 5, 7, 9], [2, 4, 6, 8, 10])))

# reduce
from functools import reduce


def add(x, y):
    return x + y


print(reduce(add, [1, 2, 3, 4, 5]))

print(reduce(lambda x, y: x + y, [1, 2, 3, 4, 5]))


# filter
# 过滤序列，用于过滤不符合条件的元素

def filter_test(n):
    return n % 2 == 1


list1 = list(filter(filter_test,[1,2,3,4,5,6,7,8,9]))
print(list1)


# sorted
# sort 与 sorted 区别：
# sort 是应用在 list 上的方法，sorted 可以对所有可迭代的对象进行排序操作。
# list 的 sort 方法返回的是对已经存在的列表进行操作，无返回值，
# 而内建函数 sorted 方法返回的是一个新的 list，而不是在原来的基础上进行的操作。

a = [5,7,6,3,4,1,2]
b = sorted(a)
print(b)

L=[('b',2),('a',1),('c',4),('d',3)]
print(sorted(L,key=lambda x:x[1]))
print(sorted(L,key=lambda x:x[0]))

students = [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]
print( sorted(students, key=lambda s: s[2]))
