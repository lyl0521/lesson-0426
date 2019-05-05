# f = open('D:/lesson-0426.yaml','rt') # endcoding='UTF-8'  解决中文乱码问题
# print(f.read())
# f.close()

# 不需释放进程的方式
with open('D:/lesson-0426.yaml','rt') as f:
    pass  # 不做任何操作

# with open('D:/lesson-0426.yaml') as f:
#     line = f.readline()
#     while line:
#         print(line)
#         line = f.readline()

# with open('D:/lesson-0426.yaml') as f:
#     for x in f:
#         print(x.strip())

# with open('D:/lesson-0426.yaml') as f:
#     for line in f.readlines():
#         print(line.strip())

# from urllib.request import urlopen
#
# with urlopen('https://movie.douban.com/top250') as f:
#     for line in f.readlines():
#         print(line.decode('UTF-8').strip())

# 	打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。
# 	也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
with open('d:/text.txt','a') as f:
    f.write('Hello,world!')

# with open('D:/text1.txt','x') as f:
#     f.write('hello world!')

with open('d:/sakura.jpg','rb') as f:
    # print(f.read())
    pass

import os

print(os.name)