# 定义一个学生类，包含三个属性（学号、姓名、成绩）均为私有的
#     分别给这三个属性定义两个方法，一个设置他的值，一个获得他的值
#     测试这些方法

class Student:

    def __init__(self,sno,name,score):
        self.__sno = sno
        self.__name = name
        self.__score = score

    def get_name(self):
        return self.__name

    def set_name(self,name):
        self.__name = name

    def get_score(self):
        return self.__score()

    def set_score(self,score):
        self.__score = score

    def get_sno(self):
        return self.__sno

    def set_sno(self,sno):
        self._sno = sno


student = Student(123,'Tom',90)
student.set_score(80)
print(student.get_score())

student.set_name('Jerry')
print(student.get_name())

student.set_sno(124)
print(student.get_sno())