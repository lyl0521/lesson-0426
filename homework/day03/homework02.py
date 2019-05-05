# 按行读取一个文件，把每一行内容存入一个list

with open('num.txt') as f:
    line = f.readline()
    list = []
    while line:
        list.append(line.strip())
        line = f.readline()
print(list)
