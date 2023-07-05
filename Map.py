from Color import Color, ColorGroup
import random


class MapNode:
    def __init__(self, _color, _min_x, _max_x, _min_z, _max_z):
        if type(_color) == ColorGroup:
            self.color = _color
        else:
            raise Exception("Map.MapNode | Incorrect type(_color): " + str(type(_color)))
        self.min_x = _min_x
        self.max_x = _max_x
        self.min_z = _min_z
        self.max_z = _max_z

    def contains(self, pos, fuzz=0, weight=0):
        x = False
        z = False
        if self.min_x <= pos.x <= self.max_x:
            x = True
        if self.min_z <= pos.z <= self.max_z:
            z = True
        if not x and (self.min_x - fuzz <= pos.x <= self.max_x + fuzz):
            if weight >= random.randint(1, 101):
                x = True
        if not z and (self.min_z - fuzz <= pos.z <= self.max_z + fuzz):
            if weight >= random.randint(1, 101):
                z = True
        return x and z

    def get_color(self):
        return self.color.get_color()


class Map:
    def __init__(self, *_nodes, **kwargs):
        self.nodes = []
        self.fuzz = 0
        self.weight = 0
        self.name = "NA"
        self.debug = None
        for node in _nodes:
            if type(node) == MapNode:
                self.nodes.append(node)
            else:
                raise Exception("Map | Attempted to create MapNode from " + str(type(node)))
        for k, v in kwargs.items():
            if k == "fuzz":
                self.fuzz = v
            elif k == "weight":
                self.weight = v
            elif k == "name":
                self.name = v
            elif k == "debug":
                self.debug = v

    def add_debug(self, _debug):
        self.debug = _debug

    def __str__(self):
        return self.name

    def pick_color(self, pos):
        viable = []
        for node in self.nodes:
            if node.contains(pos, fuzz=self.fuzz, weight=self.weight):
                viable.append(node)
        if len(viable) > 0:
            return random.choice(viable).color.get_color()
        else:
            if self.debug:
                self.debug.debug("No viable node for pos " + str(pos))
            else:
                raise Exception("No viable node for pos " + str(pos))
            return Color(0, 0, 0, 0)

    def random_color(self):
        return random.choice(self.nodes).get_color()
