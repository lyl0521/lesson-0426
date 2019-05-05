import urllib
from urllib.request import urlopen

# https://movie.douban.com/top250?start=0&filter=
# for i in range(0,275,25):
#     url = 'https://movie.douban.com/top250?start=' + str(i) + '&filter='
url = 'https://movie.douban.com/top250?start=0&filter='
i = 1
with urlopen(url) as f:
    for line in f.readlines():
        line = line.decode('UTF-8')
        if 'img width="100"' in line:
            string = 'https'
            # print(line.strip().index(str))
            # print(line.strip())
            img_url = line.strip()[line.strip().index(string):len(line.strip()) - 11]
            # print(img_url)
            name = 'D:\ProjectFile\Python\lesson-0426\img\\' + str(i) + '.jpg'
            urllib.request.urlretrieve(img_url,filename=name)
            i += 1