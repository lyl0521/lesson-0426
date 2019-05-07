# 汉诺塔问题
str1 = 'A'
str2 = 'B'
str3 = 'C'


def fn_hanoi(n, str1, str2, str3):
    if n == 1:
        print(str1, '->', str3)
    else:
        fn_hanoi(n - 1, str1, str3, str2)
        print(str1, '->', str3)
        fn_hanoi(n - 1, str2, str1, str3)
    return ''

n = int(input('请输入圆盘个数n:'))
fn_hanoi(n, str1, str2, str3)
