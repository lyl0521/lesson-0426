# print(dir('_builtins_'))

# print(abs(-1))
#
# print(max(1,5))
#
# print(min(-1,0,1,5))
#
#
# def add(x,y):
#     """
#     :param x: int
#     :param y: float
#     :return: sum..
#     """
#     return x,y
#
# print(add())


class Person:
    def __init__(myname,name):
        myname.name = name


    def sayhello(myname):
        print('my name is',myname.name)

p = Person('Bill')
print(p)

class Person1:
    def __init__(self,name):
        self.name = name
    def sayhello(self):
        print('my name is:',self.name)

p = Person1('Bill')
print(p)

class Person2:
    def __init__(self,name):
        self.name = name
    def sayhello(self):
        print('my name is:',self.name)

p = Person2('Bill')
p1 = Person2('Apple')
print(p)