class Circle:
    pi = 3.14

    def __init__(self, radius):
        self.radius = radius

    def circumference(self):
        circum = 2 * self.pi * self.radius
        return circum

    def area(self):
        araa = self.pi * self.radius**2
        return araa


circle_1 = Circle(4)
print(circle_1.circumference())
circle_2 = Circle(14)
print(circle_2.circumference())
print(circle_2.area())
