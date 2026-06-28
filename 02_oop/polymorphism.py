# Polymorphism example
class Shape:
    def area(self):
        raise NotImplementedError("Subclass must implement area")


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


for shape in [Rectangle(4, 5), Circle(3)]:
    print(type(shape).__name__, "area:", shape.area())
