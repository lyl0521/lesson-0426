# list/tuple/dict/set
# 类型转换

#列表，元组转换其他

# 转集合
list1 = [1,2,3,4,5]
tuple1 = (1,2,3,4,5)

set(list1)
set(tuple1)
print(set(list1))
print(set(tuple1))

#转字典
list1 = ['k1','k2','k3']
list2 = ['1','2','3']
dict1 = dict(zip(list1,list2))
print(dict1)

tuple1 = ('k1','k2','k3')
tuple2 = ('1','2','3')
dict2= dict(zip(tuple1,tuple2))
print(dict2)

list3 = [['key1','1'],['key2','2']]
dict3 = dict(list3)
print(dict3)
#转字符串

list1 = ['a','b','c']
str1 = ''.join(list1)
print(str1)

tuple1 = ('a','b','c')
str2 = ''.join(tuple1)
print(str2)

#字典转其他

# 字典转字符串
dict1 = {'a':1,'b':2}
str(dict1)
print(str(dict))

# 字符串转其他

#字符串转列表
s = 'apple'
list1 = list(s)
print(list1)

# 字符串转元组
tuple1 = tuple(s)
print(tuple1)

# 字符串转集合
set1 = set(s)
print(set1)

# 字符串转字典
dict1 = dict(s)
print(dict1)



