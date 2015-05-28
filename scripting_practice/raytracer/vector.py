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