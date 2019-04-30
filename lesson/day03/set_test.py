key = {'name','age','married','age'}
print(key)

key.add('test_key')

print(key)

key.remove('test_key')

print(key)

key.pop()
print(key)

name1 = {'Tom','Jerry'}
name2 = {'Jerry','Spike'}
print(name1.difference(name2))
name = name1.difference(name2)
print(name)


name1 = {'Tom','Jerry'}
name2 = {'Jerry','Spike'}
name1.difference_update(name2)
print(name1)


name1 = {'Tom','Jerry'}
name2 = {'Jerry','Spike'}
name = name1.intersection(name2)
print(name)


name1 = {'Tom','Jerry'}
name2 = {'Jerry','Spike'}
name1.intersection_update(name2)
print(name1)


name1 = {'Tom','Jerry'}
name2 = {'Jerry','Spike'}
print(name1.isdisjoint(name2))


name1 = {'Tom','Jerry'}
name2 = {'Jerry','Spike'}
print(name1.issubset(name2))

#超集  name2包含于name1 或 name2是name1的子集
name1 = {'Tom','Jerry'}
name2 = {'Jerry','Spike'}
print(name1.issuperset(name2))

#对称差集  除了交集外的全部
name1 = {'Tom','Jerry'}
name2 = {'Jerry','Spike'}
name = name1.symmetric_difference(name2)

#并集
name1 = {'Tom','Jerry'}
name2 = {'Jerry','Spike'}
name = name1.union(name2)
print(name)

#交集
name1 = {'Tom','Jerry'}
name2 = {'Jerry','Spike'}
name = name1.intersection(name2)
print(name)

#集合运算
name1 = {'Tom','Jerry'}
name2 = {'Jerry','Spike'}
print(name1 | name2)
print(name1 & name2)

#迭代
keys = {'name','age','married'}

for key in keys:
    print(key)