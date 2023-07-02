from direct.showbase.ShowBase import ShowBase
from Eye import Eye, get_random_position, get_random_hpr
from direct.directnotify.DirectNotify import DirectNotify
from panda3d.core import loadPrcFile
import sys
import random
from Square import Square
from Color import Color, ColorGroup
from Map import Map, MapNode
from Config import rotate_time
from GifMaker import GifMaker
from pathlib import Path

number_eye_variants = 4

loadPrcFile("config/Config.prc")

color_groups = {
    "Blue": ColorGroup("Blue", (13, 152, 186), (13, 81, 118), (93, 53, 252), (47, 10, 196)),
    "Green": ColorGroup("Green", (37, 162, 43), (1, 113, 1), (14, 115, 17), (2, 82, 5)),
    "Yellow": ColorGroup("Yellow", (255, 223, 0), (215, 242, 78), (218, 255, 28)),
    "White": ColorGroup("White", (248, 245, 250), (245, 247, 230)),
    "Brown": ColorGroup("Brown", (136, 104, 73), (136, 104, 73), (94, 72, 30), (84, 42, 14),
                        (99, 57, 15)),
    "Sand": ColorGroup("Sand", (246, 215, 176), (242, 210, 169), (231, 196, 150),
                       (225, 191, 146)),
    "Black": ColorGroup("Black", (19, 28, 27), (8, 7, 10), (29, 28, 31)),
    "Purple": ColorGroup("Purple", (82, 47, 129), (139, 139, 219), (48, 37, 95), (95, 44, 163),
                         (67, 13, 140)),
    "Gray": ColorGroup("Gray", (89, 82, 90), (171, 167, 181), (207, 205, 212)),
    "Light Blue": ColorGroup("Light Blue", (96, 194, 240), (22, 222, 240), (126, 228, 237),
                             (73, 112, 184)),
    "Dark Green": ColorGroup("Dark Green", (7, 38, 16), (8, 18, 11), (3, 43, 23)),
    "Red": ColorGroup("Red", (245, 41, 22), (163, 45, 34)),
    "Skin Color": ColorGroup("Skin Color", (141, 85, 36), (198, 134, 66), (224, 172, 105))
}

maps = [
    # Sunny Day
    Map(MapNode(color_groups["Blue"], -1, 1, -0.4, 1),
        MapNode(color_groups["Blue"], -1, 1, -0.4, 1),
        MapNode(color_groups["Green"], -1, 1, -1, -0.35),
        MapNode(color_groups["Green"], -1, 1, -1, -0.35),
        MapNode(color_groups["Green"], -1, 1, -1, -0.35),
        MapNode(color_groups["Green"], -1, 1, 0.7, 0.75),
        MapNode(color_groups["Yellow"], 0.5, 1, 0.5, 1),
        MapNode(color_groups["Yellow"], -1, 1, -0.5, -0.35),
        MapNode(color_groups["Red"], -1, 1, -0.5, -0.35),
        MapNode(color_groups["White"], -1, 1, 0.2, 0.75),
        MapNode(color_groups["Brown"], -1, 1, -0.5, 0.5),
        MapNode(color_groups["Brown"], -1, 1, -0.5, 0.5),
        MapNode(color_groups["Brown"], -1, 1, -0.5, 0.5),
        MapNode(color_groups["Brown"], -1, 1, -0.5, 0.5),
        fuzz=0.25, weight=60, name="Sunny Day"
        ),
    # Desert
    Map(MapNode(color_groups["Light Blue"], -1, 1, -0.4, 1),
        MapNode(color_groups["Light Blue"], -1, 1, -0.4, 1),
        MapNode(color_groups["Sand"], -1, 1, -1, -0.35),
        MapNode(color_groups["Sand"], -1, 1, -1, -0.35),
        MapNode(color_groups["Gray"], -1, 1, -1, -0.35),
        MapNode(color_groups["Yellow"], -1, -0.5, 0.5, 1),
        MapNode(color_groups["White"], -1, 1, 0.2, 0.75),
        MapNode(color_groups["Black"], -1, 1, -0.5, 0.5),
        MapNode(color_groups["Black"], -1, 1, -0.5, 0.5),
        MapNode(color_groups["Green"], -1, 1, -0.5, 0.5),
        MapNode(color_groups["Green"], -1, 1, -0.5, 0.5),
        MapNode(color_groups["Green"], -1, 1, -0.5, 0.5),
        MapNode(color_groups["Green"], -1, 1, -0.5, 0.5),
        MapNode(color_groups["Green"], -1, 1, -0.5, 0.5),
        fuzz=0.25, weight=60, name="Desert"
        ),
    # Stormy
    Map(MapNode(color_groups["Purple"], -1, 1, -0.4, 1),
        MapNode(color_groups["Purple"], -1, 1, -0.4, 1),
        MapNode(color_groups["Purple"], -1, 1, -0.4, 1),
        MapNode(color_groups["Purple"], -1, 1, -0.4, 1),
        MapNode(color_groups["Purple"], -1, 1, -0.4, 1),
        MapNode(color_groups["Green"], -1, 1, -1, -0.35),
        MapNode(color_groups["Green"], -1, 1, -1, -0.35),
        MapNode(color_groups["Dark Green"], -1, 1, -0.55, -0.35),
        MapNode(color_groups["Gray"], -1, 1, 0.2, 0.75),
        MapNode(color_groups["Yellow"], -1, 1, -0.5, 0.6),
        MapNode(color_groups["Black"], -1, 1, 0.4, 1),
        fuzz=0.25, weight=60, name="Stormy"
        ),
    # Mountain
    Map(MapNode(color_groups["Gray"], -0.75, 0.75, -1, -0.75),
        MapNode(color_groups["Black"], -0.5, 0.5, -1, -0.75),
        MapNode(color_groups["Gray"], -0.65, 0.65, -0.75, -0.5),
        MapNode(color_groups["Gray"], -0.5, 0.5, -0.5, -0.25),
        MapNode(color_groups["Gray"], -0.25, 0.25, -0.25, 0),
        MapNode(color_groups["Gray"], -0.1, 0.1, 0, 0.25),
        MapNode(color_groups["Gray"], -0.75, 0.75, -1, -0.75),
        MapNode(color_groups["Gray"], -0.65, 0.65, -0.75, -0.5),
        MapNode(color_groups["Gray"], -0.5, 0.5, -0.5, -0.25),
        MapNode(color_groups["Gray"], -0.25, 0.25, -0.25, 0),
        MapNode(color_groups["Gray"], -0.1, 0.1, 0, 0.25),
        MapNode(color_groups["Gray"], -0.75, 0.75, -1, -0.75),
        MapNode(color_groups["Gray"], -0.65, 0.65, -0.75, -0.5),
        MapNode(color_groups["Gray"], -0.5, 0.5, -0.5, -0.25),
        MapNode(color_groups["Gray"], -0.25, 0.25, -0.25, 0),
        MapNode(color_groups["Gray"], -0.1, 0.1, 0, 0.25),
        MapNode(color_groups["Blue"], -1, 1, -1, 1),
        MapNode(color_groups["Yellow"], -0.25, 0.25, 0.6, 1),
        MapNode(color_groups["White"], -1, -0.5, 0, 0.5),
        MapNode(color_groups["White"], 0.5, 1, 0, 0.5),
        MapNode(color_groups["Purple"], -1, 1, -1, 0.25),
        fuzz=0.15, weight=60, name="Mountain"
        ),
    # Love Heart
    Map(MapNode(color_groups["Red"], -0.05, 0.05, -0.6, -0.5),
        MapNode(color_groups["Red"], -0.15, 0.15, -0.5, -0.25),
        MapNode(color_groups["Red"], -0.35, 0.35, -0.25, 0),
        MapNode(color_groups["Red"], -0.6, -0.35, 0, 0.25),
        MapNode(color_groups["Red"], -0.55, -0.25, 0.25, 0.5),
        MapNode(color_groups["Red"], 0.35, 0.6, 0, 0.25),
        MapNode(color_groups["Red"], 0.3, 0.5, 0.25, 0.5),
        MapNode(color_groups["Red"], -0.05, 0.05, -0.6, -0.5),
        MapNode(color_groups["Red"], -0.15, 0.15, -0.5, -0.25),
        MapNode(color_groups["Red"], -0.35, 0.35, -0.25, 0),
        MapNode(color_groups["Red"], -0.6, -0.35, 0, 0.25),
        MapNode(color_groups["Red"], -0.55, -0.25, 0.25, 0.5),
        MapNode(color_groups["Red"], 0.35, 0.6, 0, 0.25),
        MapNode(color_groups["Red"], 0.3, 0.5, 0.25, 0.5),
        MapNode(color_groups["Red"], -0.05, 0.05, -0.6, -0.5),
        MapNode(color_groups["Red"], -0.15, 0.15, -0.5, -0.25),
        MapNode(color_groups["Red"], -0.35, 0.35, -0.25, 0),
        MapNode(color_groups["Red"], -0.6, -0.35, 0, 0.25),
        MapNode(color_groups["Red"], -0.55, -0.25, 0.25, 0.5),
        MapNode(color_groups["Red"], 0.35, 0.6, 0, 0.25),
        MapNode(color_groups["Red"], 0.3, 0.5, 0.25, 0.5),
        MapNode(color_groups["Red"], -0.05, 0.05, -0.6, -0.5),
        MapNode(color_groups["Red"], -0.15, 0.15, -0.5, -0.25),
        MapNode(color_groups["Red"], -0.35, 0.35, -0.25, 0),
        MapNode(color_groups["Red"], -0.6, -0.35, 0, 0.25),
        MapNode(color_groups["Red"], -0.55, -0.25, 0.25, 0.5),
        MapNode(color_groups["Red"], 0.35, 0.6, 0, 0.25),
        MapNode(color_groups["Red"], 0.3, 0.5, 0.25, 0.5),
        MapNode(color_groups["Light Blue"], -1, 1, -1, 1),
        MapNode(color_groups["Gray"], -1, 1, -1, 1),
        MapNode(color_groups["White"], 0.65, 0.75, 0.5, 0.65),
        fuzz=0.15, weight=60, name="Love Heart"
        )
]


class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.jxndbg = DirectNotify().newCategory("jxndbg")
        self.accept("escape", sys.exit)
        self.accept("space", self.regen)
        self.accept("r", self.render_gif)
        self.accept("m", self.make_movie)
        self.squares = []
        self.eyes = []
        self.chosen_map = random.choice(maps)
        self.generate()

    def render_gif(self):
        GifMaker(str(self.chosen_map))

    def make_movie(self):
        Path(str(self.chosen_map) + "/").mkdir(exist_ok=True)
        self.movie(namePrefix=str(self.chosen_map) + '/', duration=rotate_time, fps=5)

    def clear(self):
        for square in self.squares:
            square.delete()
        for eye in self.eyes:
            eye.delete()
        self.squares = []
        self.eyes = []

    def generate(self, _keep_square=False):
        if not _keep_square:
            for i in range(250):
                new_square = self.create_square()
                self.squares.append(new_square)
            for square in self.squares:
                square.rotate()
        else:
            for square in self.squares:
                square.color = self.chosen_map.pick_color(square.node)

        for i in range(0, random.randint(1024, 2048)):
            new_eye = self.create_eye()
            new_eye.rotate()
            self.eyes.append(new_eye)

    def create_square(self):
        square_pos = get_random_position()
        square_color = self.chosen_map.pick_color(square_pos)

        if not square_color:
            raise Exception("Could not generate square_color from chosen map!")

        new_square = Square(scale=random.randint(100, 150) / 1000, color=square_color,
                            renderer=self.render, rotate=True)
        new_square.set_pos(square_pos.x, 3, square_pos.z)
        new_square.set_hpr(get_random_hpr())
        return new_square

    def create_eye(self):
        eye_pos = get_random_position()
        eye_color = self.chosen_map.pick_color(eye_pos)
        skin_color = color_groups["Skin Color"].get_color()
        if not eye_color:
            raise Exception("Could not generate eye_color from chosen map!")
        return Eye(self.render, self.loader, self.jxndbg, random.randint(1, number_eye_variants),
                   eye_color, eye_pos, skin_color)

    def regen(self):
        self.jxndbg.debug("Regenerating <3")
        self.clear()
        self.chosen_map = random.choice(maps)
        self.jxndbg.debug("New map!: " + str(self.chosen_map))
        self.generate()


app = MyApp()
app.run()
