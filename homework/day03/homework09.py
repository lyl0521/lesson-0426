# 求一个set的最大/最小元素值

keys = {'aa','bb','abc','nd','ads','ef'}
print(keys)

keys_list = list(keys)

keys_list.sort()

print(keys_list)

print('最小值为',keys_list[0])
print('最大值位',keys_list[-1])