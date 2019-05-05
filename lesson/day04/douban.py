from urllib.request import urlopen

num = 1
for i in range(0, 10):
    url_address = 'https://movie.douban.com/top250?start=' + str(i * 25) + '&filter='
    print('正在下载第',i+1,'页')
    with urlopen(url_address) as f:
        for line in f.readlines():
            line = line.decode('UTF-8')
            if 'img width="100"' in line:
                string = 'https:'
                img_url = line.strip()[line.strip().index(string):len(line.strip()) - 11]
                print('正在下载第', num, '张')
                with urlopen(img_url) as f:
                    with open('img/' + str(num) + '.jpg', 'wb') as f1:
                        f1.write(f.read())
                        print('第', num, '张，下载完成')
                        num += 1
