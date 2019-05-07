# 继承人类编写一个学生类，为学生类添加新的属性和方法
from homework.day06.homework05 import Human

class Student(Human):

    def __init__(self, name, gender, age, sno, score):
        Human.__init__(self, name, gender, age)
        self.sno = sno
        self.score = score

    def get_score(self):
        print(self.score)
        return self.score

    def get_sno(self):
        print(self.sno)
        return self.sno

    def set_score(self, score):
        self.score = score

    def set_sno(self, sno):
        self.sno = sno

    

stu = Student('Tom', 'male', 18, 123, 90)
print(stu.get_name(), stu.get_gender(), stu.get_score(), stu.get_sno(), stu.get_age())
