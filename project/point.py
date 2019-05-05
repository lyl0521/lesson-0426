from random import randint


# 玩家掷两个骰子，每个骰子点数为1-6，如果第一次点数和为7或11，则玩家胜；
# 如果点数和为2、3或12，则玩家输庄家胜。
# 若和为其他点数，则记录第一次的点数和，玩家继续掷骰子，直至点数和等于第一次掷出的点数和则玩家胜；
# 若掷出的点数和为7则庄家胜。

point1 = randint(1, 6)
point2 = randint(1, 6)

total = point1 + point2

if total == 7 or total == 11:
    print('玩家胜')

