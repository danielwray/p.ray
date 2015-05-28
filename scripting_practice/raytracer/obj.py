__author__ = 'danielwray'

# #############################################################################
# Object classes
# Version 0.1
# #############################################################################

import scripting_practice.raytracer.vector as vector
import scripting_practice.raytracer.ray as ray


class Object(object):

    def __init__(self, r, cp, cn):
        self.ray = r
        self.compute_point = cp
        self.compute_normal = cn

    def intersection(self):
        if self.compute_point:
            if self.compute_point == 0:
                return
        elif self.compute_normal == 0:
            return
        else:
            return

class Sphere(object):

    def __init__(self, n, p, c, r):
        self.name = n
        self.position = vector.Vector(p[0], p[1], p[2]).get_vector_direct()
        self.colour = c
        self.radius = r

    def get_name(self):
        return self.name

    def get_position(self):
        return self.position[0], self.position[1], self.position[2]

    def get_colour(self):
        return self.colour

    def get_radius(self):
        return self.radius

    @staticmethod
    def intersection(r, cp, cn):
        return Object(ray.Ray.get_direction(r), cp, cn)
