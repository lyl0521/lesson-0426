# 把一个dict按key排序输出

dict = {'e':1,'b':2,'a':3,'d':4}

dict1 = sorted(dict.items(),key=lambda  dict:dict[0])
print(dict)
print(dict1)