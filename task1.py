"""task1.py"""

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def circumference(self):
        return 2 * math.pi * self.radius

    def __eq__(self, other):
        if isinstance(other, Circle):
            return self.radius == other.radius
        return False

    def __lt__(self, other):
        if isinstance(other, Circle):
            return self.circumference() < other.circumference()
        return False

    def __le__(self, other):
        if isinstance(other, Circle):
            return self.circumference() <= other.circumference()
        return False

    def __gt__(self, other):
        if isinstance(other, Circle):
            return self.circumference() > other.circumference()
        return False

    def __ge__(self, other):
        if isinstance(other, Circle):
            return self.circumference() >= other.circumference()
        return False

    def __add__(self, value):
        if isinstance(value, (int, float)):
            return Circle(self.radius + value)
        raise TypeError("Unsupported operand type(s) for +: 'Circle' and '{}'".format(type(value).__name__))

    def __sub__(self, value):
        if isinstance(value, (int, float)):
            return Circle(self.radius - value)
        raise TypeError("Unsupported operand type(s) for -: 'Circle' and '{}'".format(type(value).__name__))

    def __iadd__(self, value):
        if isinstance(value, (int, float)):
            self.radius += value
            return self
        raise TypeError("Unsupported operand type(s) for +=: 'Circle' and '{}'".format(type(value).__name__))

    def __isub__(self, value):
        if isinstance(value, (int, float)):
            self.radius -= value
            return self
        raise TypeError("Unsupported operand type(s) for -=: 'Circle' and '{}'".format(type(value).__name__))

    def __repr__(self):
        return f"Circle(radius={self.radius})"


if __name__ == "__main__":
    c1 = Circle(5)
    c2 = Circle(10)

    print(c1 == c2)
    print(c1 < c2)          
    print(c1 <= c2)          
    print(c1 > c2)           
    print(c1 >= c2)          

    c3 = c1 + 2
    print(c3)                

    c1 += 3
    print(c1)                

    c4 = c2 - 5
    print(c4)                

    c2 -= 2
    print(c2)                
