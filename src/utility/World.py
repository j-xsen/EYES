import random

from src.objects.WorldObjectHolder import WorldObjectHolder
from src.objects.Object import ObjectType
from src.utility.Functions import get_random_position
from src.objects.Cube import Cube
from src.objects.Eye import Eye
from src.utility.Map import Map
from config.Config import color_groups, min_cubes, max_cubes, min_eyes, max_eyes


class World:
    cubes = None
    eyes = None

    def __init__(self, _render, _loader, _debugger, _chosen_map, _cubes=None, _eyes=None, _name=None,
                 _do_cubes=True, _do_eyes=True):
        _debugger.debug("World | Initializing World")
        self.chosen_map = _chosen_map
        self.render = _render
        self.loader = _loader
        self.debugger = _debugger
        self.name = _name

        if _do_cubes:
            if not _cubes:
                self.cubes = WorldObjectHolder(self.chosen_map, ObjectType.CUBE)
            else:
                self.cubes = _cubes
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
        if self.cubes:
            for i in range(random.randint(min_cubes, max_cubes)):
                new_pos = get_random_position(y=7)
                new_cube = Cube(self.render, self.loader, self.debugger,
                                  _color=Map.pick_color(self.chosen_map, new_pos),
                                  scale=random.randint(150, 300) / 1000, _object_id=self.cubes.num_objects())
                new_cube.rendered_object.setPos(new_pos)
                new_cube.generate()
                self.cubes.add_object(new_cube)
            self.debugger.debug(f"World | [1/2] Generated {str(self.cubes.num_objects())} cubes")
        if self.eyes:
            for i in range(random.randint(min_eyes, max_eyes)):
                new_pos = get_random_position()
                new_eye_color = Map.pick_color(self.chosen_map, new_pos)
                new_skin_color = color_groups["Skin Color"].get_color()
                new_eye = Eye(self.render, self.loader, self.debugger, random.randint(1, 4), new_eye_color, new_pos,
                              new_skin_color, _object_id=self.eyes.num_objects())
                self.eyes.add_object(new_eye)
            self.debugger.debug(f"World | [2/2] Generated {str(self.eyes.num_objects())} eyes")
        self.debugger.debug("World | Done generating world")

    async def destroy(self):
        if self.cubes:
            self.cubes.destroy()
        self.cubes = None
        if self.eyes:
            self.eyes.destroy()
        self.eyes = None
        self.chosen_map = None
