# 一个整数，它加上100后是一个完全平方数，
# 再加上168又是一个完全平方数，请问该数是多少？

import math

for i in range(1,10000):
    if math.sqrt(i+100)%1 == 0:         #  判断该数加100后开平方是否为整数（若为整数则为完全平方数）
        if math.sqrt(i+100+168)%1 == 0:     #  判断该数再加268后是否为整数
            print(i)