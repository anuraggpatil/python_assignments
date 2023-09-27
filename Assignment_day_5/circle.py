# Create a Model for representing Circle Object 
# It should have 
    # radius 
    # area 
    # perimeter 
    # info 
    # draw 

import math

class Circle:

    def create_circle(radius):
        c=Circle()
        c.radius = radius
        return c if c.is_valid() else print(f'Cannot have a circle with radius {c.radius}\n')

    def is_valid(c):
        if isinstance(c, Circle) :
            if c.radius> 0:
                return True
        return False

    def perimeter(c):
        return 2*math.pi*c.radius if c.is_valid() else float('nan')

    def area(c):
        return math.pi*c.radius*c.radius if c.is_valid() else float('nan')

    def info(c):
        return f'Circle with radius {c.radius}\nPerimeter: {c.perimeter()}\narea: {c.area()}' if c.is_valid() else '<Invalid Circle>'

    def draw(c):
        print(c.info()) 
        print()

c1 = Circle.create_circle(3)
c2 = Circle.create_circle(-1)
c1.draw()
c1.draw()
