class ComplexNum:
    def __init__(self, a):
        self.a = a


    def __add__(self, other):
        return self.a + other.a


    def __mul__(self, other):
        return self.a * other.a


c = ComplexNum(4 - 6j)
b = ComplexNum(6 + 2j)
print(c + b)
print(c * b)