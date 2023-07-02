import random
from panda3d.core import LVector3
from Config import *


def get_random_position():
    generated_pos = LVector3(random.randint(min_pos_x, max_pos_x) / 1000, random.randint(min_pos_y, max_pos_y) / 1000,
                             random.randint(min_pos_z, max_pos_z) / 1000)
    return generated_pos


def get_random_hpr():
    generated_hpr = LVector3(random.randint(-360, 360),
                             random.randint(-360, 360),
                             random.randint(-360, 360))
    return generated_hpr
