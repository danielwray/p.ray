__author__ = 'danielwray'

# #############################################################################
# Ray classes
# Version 0.1
# #############################################################################

from scripting_practice.raytracer import vector


class Ray:

    def __init__(self, o, d):
        self.origin = o
        self.direction = d

    def set_origin(self):
        self.origin = self.origin

    def get_origin(self):
        return self.origin

    def set_direction(self):

        self.direction = vector.Vector(self.direction[0], self.direction[1], self.direction[2]).\
            get_vector().__normalize__()

    def get_direction(self):
        return self.direction[0], self.direction[1], self.direction[2]

    @staticmethod
    def dot_product(a, b):
        return vector.Vector(a[0], a[1], a[2]).__dot__([b[0], b[1], b[2]])

"""
new_ray = Ray([2.0, 1.0, 2.0], [2.0, 2.0, 4.0])
print("File: ray.py")
print("Set Direction:")
print(new_ray.set_direction())
print("Get Direction:")
print(new_ray.get_direction())
print("Dot Product:")
print(new_ray.dot_product([1.0, 3.0, 4.2], [2.0, 4.3, 4.2]))
"""