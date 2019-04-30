# . 请根据 BMI 公式，根据用户输入计算 BMI 指数，并输出测试结果

# <=18       过轻
#  ( 18,25]  正常
#  ( 25,28]  过重
#  ( 28,32]  肥胖
#  >32       严重肥胖

weight = int(input('请输入您的体重(单位：KG)：'))
height = float(input('请输入您的身高(单位：M)：'))

bml = weight/(height*height)

if bml <= 18:
    print('过轻')
elif 18 < bml <= 25:
    print('正常')
elif 25 < bml <= 28:
    print('过重')
elif 28 < bml <= 32:
    print('肥胖')
elif bml>32:
    print('严重肥胖')