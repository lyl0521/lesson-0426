class Human(object):

    def __init__(self, name, age, gender):  # this
        self.name = name
        self.__age = age
        self._gender = gender

    def fun_test(self):
        pass

    def get_name(self):
        return self.name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            raise ValueError('Error: age < 0')


# human = Human('Tom', 18)
# # human.name = 'Jerry'
#
# print(human.name, human.age)
#
# human.set_age(20)
#
# print(human.age)
#
# print(human.get_name())

tom = Human('Tom', 18, 'male')

print(tom.name)
# print(tom.__age)
# print(tom._gender)
#
print(tom.get_age())
#
tom.set_age(20)
#
print(tom.get_age())