# 把两个set中的不同元素构造为一个新的set并输出

set1 = {'name','age','gender'}
set2 = {'name','birthday','address'}

set = set1.symmetric_difference(set2)
print(set)