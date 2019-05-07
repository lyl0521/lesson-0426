# 定义函数，统计字符串中大写字母和小写字母个数

string = 'HFHPAJpdjfpfjapadPJFPjf'

def check_lower(string):
    lower = 0
    upper = 0
    for n in string:
        if n.islower():
            lower += 1
        else:
            upper +=1
    return upper,lower

print(check_lower(string))
