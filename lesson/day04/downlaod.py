import urllib
from urllib.request import urlopen

def download(url,i):
    name = 'D:\ProjectFile\Python\lesson-0426\img\\' + str(i) + '.jpg'
    urllib.request.urlretrieve(img_url, filename=name)
    i += 1
    print('第', i - 1, '张下载完成')

j = 1
for i in range(0, 100, 25):
    url = 'https://movie.douban.com/top250?start=' + str(i) + '&filter='
    with urlopen(url) as f:
        for line in f.readlines():
            line = line.decode('UTF-8')
            if 'img width="100"' in line:
                string = 'https'
                img_url = line.strip()[line.strip().index(string):len(line.strip()) - 11]
                download(img_url,j)
                print('正在下载第', j, '张')
                j += 1
