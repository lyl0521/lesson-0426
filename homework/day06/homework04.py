# 定义立方体类，属性为长度，宽度，高度，通过方法计算他的体积

class Cube:

    def __init__(self, width, height, length):
        self.width = width
        self.height = height
        self.length = length

    def volume(self):
        volume = self.width * self.height * self.length
        return volume

cube = Cube(10,10,20)
print(cube.volume())