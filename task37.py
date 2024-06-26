'''Task 37 Write a program to create an abstract class Shape with abstract methods
 calculateArea() and calculatePerimeter(). Create subclasses Circle and Triangle 
 that extend the Shape class and implement
 the respective methods to calculate the area and perimeter of each shape.'''



from abc import ABC, abstractmethod
import math

class Shape(ABC):

    @abstractmethod
    def calculateArea(self):
        pass

    @abstractmethod
    def calculatePerimeter(self):
        pass


class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def calculateArea(self):
        return math.pi * self.radius ** 2

    def calculatePerimeter(self):
        return 2 * math.pi * self.radius


class Triangle(Shape):

    def __init__(self, base, height, a, b, c):
        self.base = base
        self.height = height
        self.a = a
        self.b = b
        self.c = c

    def calculateArea(self):
        return (self.base * self.height) / 2

    def calculatePerimeter(self):
        return self.a + self.b + self.c

circle = Circle(5)
triangle = Triangle(3, 4, 3, 4, 5)

print("Area of the circle:", circle.calculateArea())
print("Perimeter of the circle:", circle.calculatePerimeter())

print("Area of the triangle:", triangle.calculateArea())
print("Perimeter of the triangle:", triangle.calculatePerimeter())