import os
import shutil

# os.remove('d:/text.txt')

if os.path.exists('text.txt'):
    os.remove('text.txt')
else:
    print('not exist')

# os.rename('img/1.jpg','01.jpg')
# shutil.copy('test.py','download_test.py')

# split ext: extension 扩展名
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]])

print(os.path.splitext('file_test.py'))

