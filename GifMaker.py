import glob
from pathlib import Path

from PIL import Image
from panda3d.core import AsyncFuture


class GifMaker(AsyncFuture):
    def __init__(self, src, output):
        AsyncFuture.__init__(self)
        self.frames = []
        self.src = src
        self.output = output

    def create_gif(self):
        Path(str(self.src + "/")).mkdir(exist_ok=True)
        for image in glob.glob(self.src + "/*.png"):
            new_frame = Image.open(image)
            self.frames.append(new_frame)
        if len(self.frames) == 0:
            raise Exception("GifMaker | Empty source " + str(self.src))

        frame_one = self.frames[0]
        frame_one.save("render/" + self.output + ".gif", format="gif", append_images=self.frames, save_all=True,
                       duration=1, loop=0,
                       )
        self.setResult(frame_one)
