import os
from enum import Enum

from direct.showbase.ShowBase import ShowBase
from direct.directnotify.DirectNotify import DirectNotify
from direct.task import Task
import sys
import random
from EYES.config.Config import rotate_time, maps, gifs_to_make, fps
from EYES.src.utility.GifMaker import GifMaker
from EYES.src.utility.World import World

from panda3d.core import VirtualFileSystem, Multifile, Filename
vfs = VirtualFileSystem.getGlobalPtr()
vfs.mount(Filename("img.mf"), ".", VirtualFileSystem.MFReadOnly)


class Stages(Enum):
    GREEN = 0,
    GENERATING = 1,
    GENERATED = 2,
    MAKING_MOVIE = 3,
    MADE_MOVIE = 4,
    RENDERING_GIF = 5,
    RENDERED_GIF = 6,
    CLEANING = 7,
    CLEANED = 8


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
        self.jxndbg.debug(f"run | self.stage: {str(self.stage)}")
        if self.stage == Stages.GREEN:
            await self.generate()
        elif self.stage == Stages.GENERATED:
            await self.make_movie()
        elif self.stage == Stages.MADE_MOVIE:
            self.render_gif()
        elif self.stage == Stages.RENDERED_GIF:
            await self.clear()
        elif self.stage == Stages.CLEANED:
            self.stage = Stages.GREEN

        if self.number_rendered >= gifs_to_make:
            return Task.done

        return Task.cont

    def batch_create(self):
        self.jxndbg.debug(f"run | Batch creating {str(gifs_to_make)} at {str(rotate_time)}s ({str(fps)}fps)")
        self.taskMgr.add(self.create_task)

    def render_gif(self):
        self.stage = Stages.RENDERING_GIF
        self.jxndbg.debug("run | Rendering gif...")
        new_gif = GifMaker("screenshots/", f"{str(self.number_rendered)} {str(self.chosen_map)} "
                                           f"{self.world.cubes.num_objects()} "
                                           f"{self.world.eyes.num_objects()}", f"{str(self.number_rendered)} "
                                                                               f"{str(self.chosen_map)}").create_gif()
        self.jxndbg.debug("run | Finished rendering gif")
        self.number_rendered += 1
        self.stage = Stages.RENDERED_GIF
        return new_gif

    def finished_making_movie(self):
        self.stage = Stages.MADE_MOVIE
        self.jxndbg.debug("run | Finished movie")
        self.stage = Stages.MADE_MOVIE

    async def make_movie(self):
        self.stage = Stages.MAKING_MOVIE
        self.jxndbg.debug("run | Making movie...")

        if not os.path.exists("screenshots/"):
            os.makedirs("screenshots/")

        for f in os.listdir('screenshots/'):
            os.remove(os.path.join('screenshots/', f))

        new_task = await self.movie(namePrefix=f"screenshots/{str(self.number_rendered)} {str(self.chosen_map)}",
                                    duration=rotate_time, fps=fps)
        self.stage = Stages.MADE_MOVIE
        return new_task

    async def clear(self):
        self.stage = Stages.CLEANING
        self.jxndbg.debug("run | Destroying world!")
        if self.world:
            await self.world.destroy()
            self.world = None
        self.jxndbg.debug("run | World destroyed!")
        self.stage = Stages.CLEANED

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
        await self.clear()
        await self.generate()
        self.jxndbg.debug("run | Done regenerating.")


app = MyApp()
app.run()
