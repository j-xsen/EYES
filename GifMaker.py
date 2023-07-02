import glob
from PIL import Image
from Config import rotate_time


class GifMaker:
    def __init__(self, src):
        frames = []
        for image in glob.glob(src + "/*.png"):
            new_frame = Image.open(image)
            frames.append(new_frame)
        frame_one = frames[0]
        frame_one.save("render/render.gif", format="gif", append_images=frames, save_all=True, duration=1, loop=0)
