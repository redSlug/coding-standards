"""
Source: https://sahandsaba.com/nine-anti-patterns-every-programmer-should-be-aware-of-with-examples.html
"""


class Shape:
    def __init__(self, shape_type, *args):
        self.shape_type = shape_type
        self.args = args

    def draw(self):
        if self.shape_type == "circle":
            center = self.args[0]
            radius = self.args[1]
            # Draw a circle...
        elif self.shape_type == "rectangle":
            pos = self.args[0]
            width = self.args[1]
            height = self.args[2]
            # Draw rectangle...


# Broken down

class Shape:
    def draw(self):
        raise NotImplemented("Subclasses should implement 'draw'.")

class Circle(Shape):
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def draw(self):
        # Draw a circle...

class Rectangle(Shape):
    def __init__(self, pos, width, height):
        self.pos = pos
        self.width = width
        self.height = height

    def draw(self):
        # Draw a rectangle...