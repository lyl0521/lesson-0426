# 一球从100米高度自由落下，每次落地后反跳回原高度的一半；
# 再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？

height = 100
distance = 0
time = 0
for time in range(1,11):
    distance += height
    height = height/2
    distance += height

print('第十次掉落后走过'+str(distance)+'米')
print('第十次掉落后反弹高度'+str(height)+'米')