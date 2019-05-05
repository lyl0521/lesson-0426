# 把三个dict合并为一个dict

dict1 = {'name':'Tom'}
dict2 = {'gender':'male'}
dict3 = {'age':18}

dict = dict1.copy()
print(dict)
dict.update(dict2)
dict.update(dict3)
print(dict)
