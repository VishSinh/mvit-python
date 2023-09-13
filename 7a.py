import math

class Shape:
    def __init__(self, name):
        self.name = name
        self.area = 0

    def show_area(self):
        print(f"The area of the {self.name} is {self.area} units")

class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def calc_area(self):
        self.area = math.pi * self.radius**2

class Rectangle(Shape):
    def __init__(self, length, breadth):
        super().__init__("Rectangle")
        self.length = length
        self.breadth = breadth

    def calc_area(self):
        self.area = self.length * self.breadth

class Triangle(Shape):
    def __init__(self, base, height):
        super().__init__("Triangle")
        self.base = base
        self.height = height

    def calc_area(self):
        self.area = 0.5 * self.base * self.height

shapes = [
    Circle(5),
    Rectangle(5, 4),
    Triangle(3, 4)
]

for shape in shapes:
    shape.calc_area()
    shape.show_area()
