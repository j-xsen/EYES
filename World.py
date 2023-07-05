import random

from WorldObjectHolder import WorldObjectHolder
from Object import ObjectType
from Functions import get_random_position
from Cube import Cube
from Eye import Eye
from Map import Map
from config.Config import color_groups


class World:
    squares = None
    eyes = None

    def __init__(self, _render, _loader, _debugger, _chosen_map, _squares=None, _eyes=None, _name=None,
                 _do_squares=True, _do_eyes=True):
        _debugger.debug("World | Initializing World")
        self.chosen_map = _chosen_map
        self.render = _render
        self.loader = _loader
        self.debugger = _debugger
        self.name = _name

        if _do_squares:
            if not _squares:
                self.squares = WorldObjectHolder(self.chosen_map, ObjectType.CUBE)
            else:
                self.squares = _squares
        if _do_eyes:
            if not _eyes:
                self.eyes = WorldObjectHolder(self.chosen_map, ObjectType.EYE)
            else:
                self.eyes = _eyes

    def __str__(self):
        if self.name:
            return self.name
        else:
            return "World"

    async def generate(self):
        self.debugger.debug("World | Generating World...")
        # async for i in async_range(250):
        number_created = 0
        if self.squares:
            for i in range(250):
                new_pos = get_random_position(y=7)
                new_square = Cube(self.render, self.loader, self.debugger,
                                  _color=Map.pick_color(self.chosen_map, new_pos),
                                  scale=random.randint(150, 300) / 1000)
                new_square.rendered_object.setPos(new_pos)
                new_square.generate()
                self.squares.add_object(new_square)
            self.debugger.debug("World | [1/2] Done generating squares")
        if self.eyes:
            for i in range(random.randint(512, 1024)):
                new_pos = get_random_position()
                new_eye_color = Map.pick_color(self.chosen_map, new_pos)
                new_skin_color = color_groups["Skin Color"].get_color()
                new_eye = Eye(self.render, self.loader, self.debugger, random.randint(1, 4), new_eye_color, new_pos,
                              new_skin_color)
                self.eyes.add_object(new_eye)
            self.debugger.debug("World | [2/2] Done generating eyes")
        self.debugger.debug("World | Done generating world")

    def destroy(self):
        if self.squares:
            self.squares.destroy()
            self.squares = None
        if self.eyes:
            self.eyes.destroy()
            self.eyes = None
        self.chosen_map = None
