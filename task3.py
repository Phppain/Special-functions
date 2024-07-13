"""task3.py"""

class Airplane:
    def __init__(self, airplane_type, max_passengers, current_passengers=0):
        self.airplane_type = airplane_type
        self.max_passengers = max_passengers
        self.current_passengers = current_passengers

    def __eq__(self, other):
        if isinstance(other, Airplane):
            return self.airplane_type == other.airplane_type
        return False

    def __add__(self, passengers):
        if isinstance(passengers, int):
            new_passengers = self.current_passengers + passengers
            if new_passengers > self.max_passengers:
                raise ValueError("Exceeding maximum passenger capacity")
            return Airplane(self.airplane_type, self.max_passengers, new_passengers)
        raise TypeError("Unsupported operand type(s) for +: 'Airplane' and '{}'".format(type(passengers).__name__))

    def __sub__(self, passengers):
        if isinstance(passengers, int):
            new_passengers = self.current_passengers - passengers
            if new_passengers < 0:
                raise ValueError("Negative passenger count not allowed")
            return Airplane(self.airplane_type, self.max_passengers, new_passengers)
        raise TypeError("Unsupported operand type(s) for -: 'Airplane' and '{}'".format(type(passengers).__name__))

    def __iadd__(self, passengers):
        if isinstance(passengers, int):
            self.current_passengers += passengers
            if self.current_passengers > self.max_passengers:
                raise ValueError("Exceeding maximum passenger capacity")
            return self
        raise TypeError("Unsupported operand type(s) for +=: 'Airplane' and '{}'".format(type(passengers).__name__))

    def __isub__(self, passengers):
        if isinstance(passengers, int):
            self.current_passengers -= passengers
            if self.current_passengers < 0:
                raise ValueError("Negative passenger count not allowed")
            return self
        raise TypeError("Unsupported operand type(s) for -=: 'Airplane' and '{}'".format(type(passengers).__name__))

    def __lt__(self, other):
        if isinstance(other, Airplane):
            return self.max_passengers < other.max_passengers
        return False

    def __le__(self, other):
        if isinstance(other, Airplane):
            return self.max_passengers <= other.max_passengers
        return False

    def __gt__(self, other):
        if isinstance(other, Airplane):
            return self.max_passengers > other.max_passengers
        return False

    def __ge__(self, other):
        if isinstance(other, Airplane):
            return self.max_passengers >= other.max_passengers
        return False

    def __repr__(self):
        return f"Airplane(type={self.airplane_type}, max_passengers={self.max_passengers}, current_passengers={self.current_passengers})"


if __name__ == "__main__":
    a1 = Airplane("Boeing 737", 200, 150)
    a2 = Airplane("Airbus A320", 180, 120)
    a3 = Airplane("Boeing 737", 200, 100)

    print(a1 == a2)
    print(a1 == a3)

    print(a1 + 30)
    print(a1 - 50)

    a1 += 20
    print(a1)

    a1 -= 50
    print(a1)

    print(a1 > a2)
    print(a1 < a2)
    print(a1 >= a2)
    print(a1 <= a2)
