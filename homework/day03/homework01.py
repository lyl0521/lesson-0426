# 读取一个文本文件的前n行

with open('num.txt') as f:
    line = f.readline()
    x = 0
    while x < 3:   #  通过while循环来控制输出行数
        print(line.strip())
        x += 1
        line = f.readline()
