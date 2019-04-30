d1 = {'key1':1,'key2':2,'key3':3}
d2 = {'key1':2,'key2':2}

for key in d1.keys():
    for key2 in d2.keys():
        if d1[key] == d2[key2] and key == key2:
            print(key,d1[key])

