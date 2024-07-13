"""task4.py"""

class Flat:
    def __init__(self, area, price):
        self.area = area
        self.price = price

    def __eq__(self, other):
        if isinstance(other, Flat):
            return self.area == other.area
        return False

    def __ne__(self, other):
        if isinstance(other, Flat):
            return self.area != other.area
        return False

    def __lt__(self, other):
        if isinstance(other, Flat):
            return self.price < other.price
        return False

    def __le__(self, other):
        if isinstance(other, Flat):
            return self.price <= other.price
        return False

    def __gt__(self, other):
        if isinstance(other, Flat):
            return self.price > other.price
        return False

    def __ge__(self, other):
        if isinstance(other, Flat):
            return self.price >= other.price
        return False

    def __repr__(self):
        return f"Flat(area={self.area}, price={self.price})"


if __name__ == "__main__":
    f1 = Flat(60, 30000)
    f2 = Flat(75, 35000)
    f3 = Flat(60, 28000)

    print(f1 == f2)
    print(f1 == f3)
    print(f1 != f2)
    print(f1 != f3)

    print(f1 > f2)
    print(f1 < f2)
    print(f1 >= f3)
    print(f1 <= f3)
