# 求一个字符串List中，字符串长度大于2，且首尾字符相同的元素个数
# ['a','xy','alabama','101']

list = ['a','xy','alabama','101']
counter = 0
for element in list:
    if len(element) > 2:
        if element[0] == element[-1]:
            counter += 1
            print(element)
print('复合要求的字符串有'+str(counter)+'个')