class Square:
    sides = 4

    def area(self):
        return self.height * self.height

my_shape = Square()
my_shape.height = 10
print(my_shape.area())


class Square2:
    sides = 4

    def __init__(self):
        self.height2 = 0

    def area(self):
        return self.height2 * self.height2

my_shape2 = Square2()
my_shape2.height2 = 10
print(my_shape2.area())