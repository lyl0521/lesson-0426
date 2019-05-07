# 定义一个人类，包含姓名，性别，年龄等信息
#     所有变量必须私有，其他类只能通过该类的方法进行获取和修改
#     实例化一个人类，试着通过该类的方法修改实例化的人的信息


class Human:

    def __init__(self, name, gender, age):
        self.__name = name
        self.__gender = gender
        self.__age = age

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

    def get_name(self):
        return self.__name

    def set_name(self,name):
        self.__name = name

    def get_gender(self):
        return self.__gender

    def set_gender(self,gender):
        self.__gender = gender


human = Human('Tom','male',18)

human.set_name('Marry')
human.set_age(20)
human.set_gender('female')
print(human.get_name(),human.get_age(),human.get_gender())