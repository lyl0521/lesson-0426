# 查询一篇英文文章的最长单词

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

longest = ''
for word in words:
    if len(word) > len(longest):
        longest = word
print(longest)