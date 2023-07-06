import random
from panda3d.core import LVecBase4f


class Color(LVecBase4f):
    def __init__(self, _r, _g, _b, _a=1):
        LVecBase4f.__init__(self, _r/255, _g/255, _b/255, _a)

    def get_color(self):
        return self

    def __str__(self):
        return str(self.x*255) + ", " + str(self.y*255) + ", " + str(self.z*255) + "," + str(self.w)


class ColorGroup:
    def __init__(self, _name, *_colors):
        self.name = _name
        self.colors = []

        for color in _colors:
            self.colors.append(Color(color[0], color[1], color[2]))

    def get_color(self):
        if len(self.colors) == 0:
            raise Exception("Attempted to get color of empty color group " + self.name)
        return random.choice(self.colors)
