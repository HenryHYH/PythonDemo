""""运算符重载"""


class Vector:
    """Vector"""

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return "Vector(%d, %d)" % (self.a, self.b)

    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)


if __name__ == "__main__":
    v1 = Vector(1, 2)
    v2 = Vector(3, -2)
    print(v1 + v2)
