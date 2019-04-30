for i in range(0, 10):  #
    print(i)

fruits = ['apple', 'banana', 'orange']  # list 列表
# fruits = []  # list 列表
for fruit in fruits:
    print(fruit)
    if fruit == 'banana':
        break
else:  # 循环正常结束后的处理：没有 break
    print('else...')

is_found = False
for fruit in fruits:
    print(fruit)
    if fruit == 'watermelon':
        # proceed...
        print('found watermelon.')
        is_found = True
        break
# else:  # 循环正常结束后的处理：没有 break
#     print('not found watermelon.')

if not is_found:
    print('not found watermelon.')

# 语法糖 syntactic sugar: 在没有改变语言功能的前提下，是程序的写法更加简洁
# 语法： 盐/糖精/海洛因