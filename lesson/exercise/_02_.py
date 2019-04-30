# 判断101-200之间有多少个素数，并输出所有素数。
# 素数：只能被1和它本身整除的正整数（1不是素数）

counter = 0
for i in range(101,201):
    for j in range(2,i):
        if i % j ==0:
            print(str(i)+'不是素数')
            break
    else:
        print(str(i)+'是素数')