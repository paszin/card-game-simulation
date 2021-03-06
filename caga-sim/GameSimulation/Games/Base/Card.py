class Card:

    def __init__(self, symbol=None, number=None):
        self.symbol = symbol
        self.number = number
        self.valid = True # some cards have an effect only once

    def __str__(self):
        return f"|{self.symbol or ''}{self.number}|"

    def __repr__(self):
        return f"|{self.symbol or ''}{self.number}|"

    def __eq__(self, other):
        if type(other) == int:
            return self.number == other
        return self.symbol == other.symbol and self.number == other.number

    def __lt__(self, other):
        return self.number < other.number

    def __le__(self, other):
        return self.number <= other.number

    def __gt__(self, other):
        return self.number > other.number

    def __ge__(self, other):
        return self.number >= other.number

    def __add__(self, other):
        if type(other) == int:
            return Card(number=self.number + other)
        else:
            return Card(number=self.number + other.number)

    def __sub__(self, other):
        if type(other) == int:
            return Card(number=self.number - other)
        else:
            return Card(number=self.number - other.number)

    def __abs__(self):
        return abs(self.number)
