# 输入某年某月某日，判断这一天是这一年的第几天？
# (闰年： 西元年份除以400余数为0的，或者除以4为余数0且除以100不为余数0的，为闰年。)

year = int(input('请输入要判断的年份:'))

if year % 400 == 0 or ((year % 4 == 0) and (year % 100 !=0)):
    print(str(year) + '年是闰年')
else:
    print(str(year)+ '年不是闰年')