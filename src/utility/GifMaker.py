import glob
from pathlib import Path

from PIL import Image
from config.Config import fps


class GifMaker:
    def __init__(self, src, output, srcprefix):
        self.frames = []
        self.src = src
        self.srcprefix = srcprefix
        self.output = output

    def create_gif(self):
        self.frames = []  # naughty naughty
        Path(str(self.src + "/")).mkdir(exist_ok=True)
        for image in glob.glob(self.src + f"/{self.srcprefix}*.png"):
            new_frame = Image.open(image)
            self.frames.append(new_frame)
        if len(self.frames) == 0:
            raise Exception("GifMaker | Empty source " + str(self.src))

        frame_one = self.frames[0]
        frame_one.save("render/" + self.output + ".gif", format="gif", append_images=self.frames, save_all=True,
                       duration=40, loop=0)
