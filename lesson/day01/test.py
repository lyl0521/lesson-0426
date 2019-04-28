print('hello')

# comment

"""
comments   推荐
"""

'''
comments
'''

print(0xff)

print(1.234e5)

print('complex', 1 + 2j)

print(complex(1, 2))

print('complex', complex(1, 2).conjugate())

print('Tom\'s name')
print(r'Tom\'s name')  # r  raw  原样输出

print('line\nline')
print("""
    白日依山尽，
    黄河入海流
""")

print('a', 'b', 'c')
print('a' + 'b' + 'c')

# print(input())

s = 'hello, world!'

print(s[0:2])

print('h' in s)

print(s.capitalize())

print(s.center(20, '-'))

print(s.zfill(20))

print(s.count('l'))

print(s.endswith('!', 10, 13))
print(s.endswith('!', 1, 3))
print(s)
print(s.startswith('h', 0, 3))

print(s.find(',', 2, 10))
print(s.find(',', 10, 13))

str = 'H\tello, world!'
print(str)
print(str.expandtabs(tabsize=8))

print(1 and 0)
print(1 and 1)
print(1 or 0)
print(1 or 1)
print(0 or 1)
print(0 or 0)
print(0 and 0)
print(0 and 1)

string = 'asdfqwer'
str = 'H\tello, world!'
print(string.isalnum())  # 不包含空格 输出true
print(str.isalnum())  # 包含空格则输出false

print(string.isalpha())

s = 'Hello world!'
print(s[:6] + 'runoob')
print('a\000b')  # \000 空

print("My name is %s and weight is %d kg!" % ('Zara', 60))

print(s.find('l', 0, 3))

print(s.isalpha())  # 至少有一个字符，而且所有字符都是字母返回true
print('asdzxc'.isalpha())

print('123456789'.isdecimal())  # 只包含十进制数字

x = 0xff
print('123'.isdigit())  # 只包含数字

s = 'Hello world'
print(s.islower())
print('asdad'.islower())  # 只包含小写


# 只包含空格
print(' '.isspace())
print('as d'.isspace())
# 只包含标题化
str = 'hello world'
str1 = str.title()
print(str1)
print(str.istitle())
print(str1.istitle())
# 至少有一个大写字母 而且全都是大写
str = 'ASDJ'
str1 = 'asdf'

print(str.isupper())
print(str1.isupper())
# 以str为分隔符 分隔join（）中的字符串
str = '-'
print(str.join('IJK'))

# 左对齐并以空格补全长度
print('hello'.ljust(15) + '1')

print('HJK'.lower())
# 去掉字符串左边的空格
print('      hello'.lstrip())

intab = "aeiou"
outtab = "12345"
deltab = "thw"
trantab1 = str.maketrans(intab, outtab)  # 创建字符映射转换表
trantab2 = str.maketrans(intab, outtab, deltab)  # 创建字符映射转换表，并删除指定字符
test = "this is string example....wow!!!"

print(test.translate(trantab1))
print(test.translate(trantab2))

print(max('abc'))
print(min('abc'))
# 返回一个3元的元组，第一个为分隔符左边的子串，
# 第二个为分隔符本身，第三个为分隔符右边的子串。
str = "www.baidu.com"
print(str.partition("."))

print('hello'.replace('l', 'L'))
print('hello'.replace('l', 'L', 1))

str1 = "this is string example....wow!!!"
str2 = "is"
print(str1.rfind(str2))
print(str1.find(str2))
# 去掉尾部空格
print('hello'.rstrip() + '1')

print(str1.split(' '))
# 根据字符串进行分割
print(str1.split(' ', 1))
# 第一次分隔后，后面的分成1（num）部分

str1 = 'ab c\n\nde fg\rkl\r\n'
print(str1.splitlines())
# keepends -- 在输出结果里是否保留换行符('\r', '\r\n', \n')，
# 默认为 False，不包含换行符，如果为 True，则保留换行符。
str2 = 'ab c\n\nde fg\rkl\r\n'
print(str2.splitlines(True))


print('  hello  '.strip())


