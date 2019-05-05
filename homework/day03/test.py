import string

with open('news.txt') as f:
    lines = f.readlines()
    for i in range(len(lines)):
        list = []
        for word in lines[i].split():
            word = word.strip(string.whitespace)
            list.append(word)
    print(list)