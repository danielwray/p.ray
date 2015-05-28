__author__ = 'danielwray'

# #############################################################################
# Main classes
# Version 0.1
# #############################################################################


import scripting_practice.raytracer.obj as obj
import scripting_practice.raytracer.world as world
import scripting_practice.raytracer.vector as vector

class Main:

    def __init__(self, w, c, l, hy, wx):
        self.world = world.World().new_world(w)
        self.camera = c
        self.light = l
        self.height = hy
        self.width = wx
        self.object_list = []

    def rendering_loop(self):
        for px in range(0, self.width):
            print("Completion: ", px)
            for py in range(0, self.height):
                pass

    def create_objects(self, o):
        self.object_list.append(o)
        for objects in self.object_list:
            origin_to_w_origin = vector.Vector(world.World().get_origin()[0], world.World().get_origin()[1],
                                               world.World().get_origin()[2]).get_vector().a_to_b(objects.get_position())
            return origin_to_w_origin


# List of settings below
world_colour = "black"
camera_position = [1.0, 2.0, 3.0]
camera_direction = [2.0, -1.0, 4.0]
light_position = [1.0, 3.0, 5.0]
light_intensity = 10.0
window_height = 2
window_width = 2
object001 = obj.Sphere("Sphere.001", [1.0, 2.5, 1.0], [1.0, 1.0, 0.5], 2.0)


scene = Main(world_colour, camera_position, light_position, window_height, window_width)
print(scene.rendering_loop())
print(scene.create_objects(object001))
print(obj.Sphere.get_name(object001))
print(obj.Sphere.get_colour(object001))
print(obj.Sphere.get_position(object001))
