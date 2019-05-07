# 定义函数，把一个list的元素去重，返回新的list
list1 = [1,2,5,3,1,7,6,3,9,5,4,9,2]


def remove_rep(string):
    list1 = list(set(string))
    return list1


print(remove_rep(list1))