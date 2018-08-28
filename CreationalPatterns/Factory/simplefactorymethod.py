
from __future__ import generators
import random


class Shape(object):
    #create based on class name

    @staticmethod
    def factory(type):
        if type == 'Circle':
            return Circle()
        if type == 'Square':
            return Square()
        assert 0, 'Bad shape creation %s' % type


class Circle(Shape):
    def draw(self):
        print("Circle.draw")

    def erase(self):
        print("Circle.erase")


class Square(Shape):
    def draw(self):
        print("Square.draw")

    def erase(self):
        print("Square.erase")


# Generate shape name strings:
def shapeNameGen(n):
    types = Shape.__subclasses__()
    for i in range(n):
        yield random.choice(types).__name__


shapes = [Shape.factory(i) for i in shapeNameGen(2)]

print(shapes)
for shape in shapes:
    shape.draw()
    shape.erase()