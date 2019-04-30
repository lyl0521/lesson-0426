d = {'name':'Tom','age':19,'gender':'male','isMarried':False}

print(d)

print(d['name'])

d = {}

d = dict(key=123)
d['test'] = False

# d = {}.fromkeys(['name','age'])
# d = {}.fromkeys(['name','age'],'value')
seq = ('Google','Runoob','Taobao')
d = {}.fromkeys(seq)

print(d)

print(d.get('name1','default value'))
#  查找键值为‘name1’的值，如果没有输出‘default value’

d = {'key':'value'}
print(d)

d['key'] = 'new value'
print(d)

d['new_key'] = 'new value1'
d['new_key'] = 'new value2'

print(d)

del d['new_key']
# d.pop('key')
print(d)

d_new = d.copy()
print(d_new)
print(d)

d = {'name': 'Tom', 'age': 18, 'married': False}

print(d)

for key in d.keys():
    print(key,d[key])

for value in d.values():
    print(value)

for k,v in d.items():
    print(k,v)

list1 = ['list']
d = {list:'value'}
print(d)