import os

print(os.path.abspath('.'))

print(os.getcwd())

print(os.path.join('d:/test','test','test.txt'))

# print(os.makedirs(os.path.join('.','new_dir','sub_dir')))
# rmdir 删除文件夹时，文件夹必须为空
# print(os.rmdir(os.path.join('.','new_dir','sub_dir')))
# print(os.rmdir(os.path.join('.','new_dir')))

print(os.path.split('new_dir/sub_dir/test.txt'))
# ('new_dir/sub_dir', 'test.txt')

print(os.path.splitext('google.com.png'))
# ('google.com', '.png')

#当前文件夹下的目录列表
print([x for x in os.listdir('.') if os.path.isdir(x)])