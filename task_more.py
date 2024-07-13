"""task_more.py"""

class Roman:
    roman_to_int_map = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    int_to_roman_map = [
        (1000, 'M'),
        (900, 'CM'),
        (500, 'D'),
        (400, 'CD'),
        (100, 'C'),
        (90, 'XC'),
        (50, 'L'),
        (40, 'XL'),
        (10, 'X'),
        (9, 'IX'),
        (5, 'V'),
        (4, 'IV'),
        (1, 'I')
    ]

    def __init__(self, value):
        if isinstance(value, str):
            self.value = self.roman_to_int(value)
        elif isinstance(value, int):
            self.value = value
        else:
            raise TypeError("Unsupported type for Roman number")

    def __add__(self, other):
        if isinstance(other, Roman):
            return Roman(self.value + other.value)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Roman):
            return Roman(self.value - other.value)
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, Roman):
            return Roman(self.value * other.value)
        return NotImplemented

    def __truediv__(self, other):
        if isinstance(other, Roman):
            return Roman(self.value // other.value)
        return NotImplemented

    def __repr__(self):
        return f"Roman('{self.int_to_roman(self.value)}')"

    def __str__(self):
        return self.int_to_roman(self.value)

    @staticmethod
    def roman_to_int(roman):
        result = 0
        prev_value = 0
        for char in reversed(roman):
            value = Roman.roman_to_int_map[char]
            if value < prev_value:
                result -= value
            else:
                result += value
            prev_value = value
        return result

    @staticmethod
    def int_to_roman(number):
        result = []
        for value, numeral in Roman.int_to_roman_map:
            while number >= value:
                result.append(numeral)
                number -= value
        return ''.join(result)


if __name__ == "__main__":
    r1 = Roman("X")
    r2 = Roman("V")

    print(r1 + r2)
    print(r1 - r2)
    print(r1 * r2)
    print(r1 / r2)

    r3 = Roman(20)
    r4 = Roman(3)

    print(r3 + r4)
    print(r3 - r4)
    print(r3 * r4)
    print(r3 / r4)
