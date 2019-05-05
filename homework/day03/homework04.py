# 查找出文章中出现次数最多的单词

from collections import Counter

string = ''
with open('news.txt') as f:
    for line in f.readlines():
        string += line.strip()

strings = string.replace('"',' ')
strings = strings.replace(',','')
strings = strings.replace('.',' ')
words = strings.split(' ')

while '' in words:
    words.remove('')

times = Counter(words)

most = times.most_common(1)

print('出现次数最多的单词为'+most[0][0],'共出现'+most[0][0]+'次')


