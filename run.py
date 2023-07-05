import os
from enum import Enum

from direct.interval.IntervalGlobal import Sequence

from direct.interval.FunctionInterval import Func
from direct.showbase.ShowBase import ShowBase

from direct.directnotify.DirectNotify import DirectNotify
from direct.task import Task
from panda3d.core import loadPrcFile
import sys
import random
from config.Config import rotate_time, maps
from GifMaker import GifMaker
from World import World

number_eye_variants = 4

loadPrcFile("config/Config.prc")


class Stages(Enum):
    GREEN = 0,
    GENERATING = 1,
    GENERATED = 2,
    MAKING_MOVIE = 3,
    MADE_MOVIE = 4,
    RENDERING_GIF = 5,
    RENDERED_GIF = 6,


class MyApp(ShowBase):

    stage = Stages.GREEN
    world = None
    chosen_map = None
    number_rendered = 0

    def __init__(self):
        ShowBase.__init__(self)

        # debug
        self.jxndbg = DirectNotify().newCategory("jxndbg")

        # keybinds
        self.accept("escape", sys.exit)
        self.accept("space", self.regen)
        self.accept("r", self.render_gif)
        self.accept("m", self.make_movie)
        self.accept("x", self.batch_create)

        self.taskMgr.add(self.generate())

    async def create_task(self, task):
        if self.stage == Stages.GREEN:
            await self.generate()
        elif self.stage == Stages.GENERATED:
            await self.make_movie()
        elif self.stage == Stages.MADE_MOVIE:
            self.render_gif()
        elif self.stage == Stages.RENDERED_GIF:
            self.stage = Stages.GREEN
            self.number_rendered += 1

        if self.number_rendered > 3:
            return Task.done

        return Task.cont

    def batch_create(self):
        self.taskMgr.add(self.create_task)

    def render_gif(self):
        self.stage = Stages.RENDERING_GIF
        self.jxndbg.debug("run | Rendering gif...")
        new_gif = GifMaker("screenshots/", str(self.chosen_map) + " "
                           + str(self.number_rendered)).create_gif()
        self.jxndbg.debug("run | Finished rendering gif")
        self.stage = Stages.RENDERED_GIF
        return new_gif

    def finished_making_move(self):
        self.stage = Stages.MADE_MOVIE
        self.jxndbg.debug("run | Finished movie")
        self.stage = Stages.MADE_MOVIE

    async def make_movie(self):
        self.stage = Stages.MAKING_MOVIE
        self.jxndbg.debug("run | Making movie...")
        if not os.path.exists("screenshots/"):
            os.makedirs("screenshots/")
        new_task = await self.movie(namePrefix="screenshots/", duration=rotate_time, fps=5)
        self.stage = Stages.MADE_MOVIE
        return new_task

    def clear(self):
        self.jxndbg.debug("run | Destroying world!")
        if self.world:
            self.world.destroy()
            self.world = None
        self.jxndbg.debug("run | World destroyed!")

    async def generate(self):
        self.stage = Stages.GENERATING
        self.jxndbg.debug("run | Generating world!")
        self.chosen_map = random.choice(maps)
        self.jxndbg.debug("run | New map!: " + str(self.chosen_map))
        self.world = World(self.render, self.loader, self.jxndbg, self.chosen_map)
        await self.world.generate()
        self.jxndbg.debug("run | Done generating world!")
        self.stage = Stages.GENERATED

    async def generate_task(self, task):
        await self.generate()
        return Task.done

    async def regen(self):
        self.jxndbg.debug("run | Regenerating <3")
        self.clear()
        await self.generate()
        self.jxndbg.debug("run | Done regenerating.")


app = MyApp()
app.run()
