# 求1+2!+3!+…+20!的和。


sum = 0

for i in range(1,21):
    num = 1
    for j in range(1,i+1):
        num *= j
        print(j,end='*')
    print()
    sum += num

print(sum)