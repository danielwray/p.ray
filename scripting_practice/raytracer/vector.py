__author__ = 'danielwray'

# #############################################################################
# Vector classes
# Version 0.2
# #############################################################################

from math import sqrt


class Vector:
    def __init__(self, x, y, z):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    def __add__(self, b):
        return self.x + b[0], self.y + b[1], self.z + b[2]

    def __sub__(self, b):
        return self.x - b[0], self.y + b[1], self.z - b[2]

    def __mul__(self, b):
        return self.x * b, self.y * b, self.z * b

    def __div__(self, b):
        if self.z and self.x and self.y == float(0):
            self.x = 0.001
            self.y = 0.001
            self.z = 0.001
            return self.x / b, self.y / b, self.z / b
        else:
            return self.x / b, self.y / b, self.z / b

    def __dot__(self, b):
        return self.x * b[0] + self.y * b[1] + self.z * b[2]

    def __length__(self):
        return sqrt(self.x * self.x + self.y * self.y + self.z * self.z)

    def __normalize__(self):
        return self.__div__(self.__length__())

    def __cross__(self, b):
        return self.x * b[2] - self.z * b[1], self.z * b[0] - self.x * b[2], self.x * b[1] - self.y * b[0]

    def is_orthogonal(self, a, b):
        if Vector.get_vector(a).__dot__(b) == 0.0:
            return 0.0
        else:
            return self.x, self.y, self.z

    def a_to_b(self, b):
        return self.x.__sub__(b[0]), self.y.__sub__(b[1]), self.z.__sub__(b[2])

    def set(self, b):
        self.x = float(b)
        self.y = float(b)
        self.z = float(b)
        return self.x, self.y, self.z

    def negative(self):
        return -self.x, -self.y, -self.z

    def null(self):
        self.x = float(0)
        self.y = float(0)
        self.z = float(0)
        return self.x, self.y, self.z

    def get_vector(self):
        return Vector(self.x, self.y, self.z)

    def get_vector_direct(self):
        return self.x, self.y, self.z

"""
When calling the above use vector.Vector.get_vector(x, y, z).__function__()
The "get_vector()" call will initialise a new vector

test = Vector(1.0, 0.1, 2.0)
print("File: vector.py")
print("Addition:")
print(test.get_vector().__add__([1.0, 3.0, 4.2]))
print("Subtraction:")
print(test.get_vector().__sub__([2.0, 3.5, 5.0]))
print("Multiplication:")
print(test.get_vector().__mul__(2.4))
print("Division:")
print(test.get_vector().__div__(7.18))
print("Dot Product:")
print(test.get_vector().__dot__([1.0, 5.4, 3.4]))
print("Length:")
print(test.get_vector().__length__())
print("Normalize:")
print(test.get_vector().__normalize__())
print("Cross Product:")
print(test.get_vector().__cross__([2.0, 5.4, 3.5]))
print("Set:")
print(test.get_vector().set(2.5))
print("Negative:")
print(test.get_vector().negative())
print("Null (0.0):")
print(test.get_vector().null())
print("Is Orthogonal:")
print(test.get_vector().is_orthogonal(test, [0.0, 0.0, 1.0]))
"""
