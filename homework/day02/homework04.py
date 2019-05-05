# 把一个tuple转为字符串


s = 'xxxxxx'

print(list(s))
print(tuple(s))
print(tuple(list(s)))

print(list(tuple(s)))

print(''.join(tuple(s)))
print(''.join(list(s)))
print(str(tuple(s)))

y = 'Tom'
z = ('TOM','jERRY')
print(tuple(z))     # ('TOM', 'jERRY')   元祖
print(''.join(tuple(z)))  #TOMjERRY
print(str(tuple(z)))  #  ('TOM', 'jERRY')     字符串
print(z.__str__())  #('TOM', 'jERRY')       字符串
print(list(z))      #['TOM', 'jERRY']       列表