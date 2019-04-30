names = ['Tom','Jerry']

print(names)

print(names[0])

print(names[-1])  #  last element
print(names[-2])

print(len(names))

names.append('Spike')

print(names)

names.insert(2,'Tyke')

print(names)

names[3] = 'Spike'

print(names)

names.pop()   #  默认删除最后一个元素
names.pop(0)   #  写入参数删除对应元素

print(names)

superstar = ['Tom','Jerry']
names = [superstar,'Spike']
print(names)
names.clear()

print(names)

names = superstar.copy()
print(names)

names.append('Spike')

print(superstar.index('Jerry'))

names.remove('Spike')

names.reverse()

print(names)

names.sort(reverse=True)
print(names)

for name in names:
    print(name)