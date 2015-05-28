__author__ = 'danielwray'

# #############################################################################
# World classes
# Version 0.1
# #############################################################################

class World:

    def __init__(self):
        self.origin = [0.0, 0.0, 0.0]
        self.background = 0

    def new_world(self, background):
        self.background = background
        return self.origin, self.background

    def get_origin(self):
        return self.origin[0], self.origin[1], self.origin[2]

    def get_background(self):
        return self.background
