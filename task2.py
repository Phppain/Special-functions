"""task2.py"""

class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        if isinstance(other, Complex):
            return Complex(self.real + other.real, self.imag + other.imag)
        raise TypeError("Unsupported operand type(s) for +: 'Complex' and '{}'".format(type(other).__name__))

    def __sub__(self, other):
        if isinstance(other, Complex):
            return Complex(self.real - other.real, self.imag - other.imag)
        raise TypeError("Unsupported operand type(s) for -: 'Complex' and '{}'".format(type(other).__name__))

    def __mul__(self, other):
        if isinstance(other, Complex):
            real = self.real * other.real - self.imag * other.imag
            imag = self.real * other.imag + self.imag * other.real
            return Complex(real, imag)
        raise TypeError("Unsupported operand type(s) for *: 'Complex' and '{}'".format(type(other).__name__))

    def __truediv__(self, other):
        if isinstance(other, Complex):
            denom = other.real**2 + other.imag**2
            if denom == 0:
                raise ZeroDivisionError("division by zero")
            real = (self.real * other.real + self.imag * other.imag) / denom
            imag = (self.imag * other.real - self.real * other.imag) / denom
            return Complex(real, imag)
        raise TypeError("Unsupported operand type(s) for /: 'Complex' and '{}'".format(type(other).__name__))

    def __repr__(self):
        return f"Complex({self.real}, {self.imag})"

    def __str__(self):
        if self.imag >= 0:
            return f"{self.real} + {self.imag}i"
        else:
            return f"{self.real} - {abs(self.imag)}i"


if __name__ == "__main__":
    c1 = Complex(2, 3)
    c2 = Complex(1, 4)

    print("c1:", c1)
    print("c2:", c2)

    print("c1 + c2:", c1 + c2)
    print("c1 - c2:", c1 - c2)
    print("c1 * c2:", c1 * c2)
    print("c1 / c2:", c1 / c2)
