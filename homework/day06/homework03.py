# 定义一个类，实现求三角形的周长和面积
from math import sqrt


class Triangle:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_valid(self):
        return self.a + self.b > self.c and self.b + self.c > self.a and self.a + self.c > self.b

    def perimeter(self):
        perimeter = self.a + self.b + self.c
        return perimeter

    def area(self):
        s = (self.a + self.b + self.c) / 2
        area = sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
        return area


a, b, c = 3, 4, 5
triangle = Triangle(a,b,c)
if triangle.is_valid():
    print(triangle.perimeter())
    print(triangle.area())
else:
    print('无法构成三角形')
