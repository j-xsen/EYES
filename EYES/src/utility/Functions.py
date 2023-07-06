import random
from panda3d.core import LVector3
from EYES.config.Config import *


def get_random_position(x=None, y=None, z=None):
    generated_pos = LVector3(random.randint(min_pos_x, max_pos_x) / 1000, random.randint(min_pos_y, max_pos_y) / 1000,
                             random.randint(min_pos_z, max_pos_z) / 1000)

    if x:
        generated_pos.x = x
    if y:
        generated_pos.y = y
    if z:
        generated_pos.z = z

    return generated_pos


def get_random_hpr(h=None, p=None, r=None):
    generated_hpr = LVector3(random.randint(-360, 360),
                             random.randint(-360, 360),
                             random.randint(-360, 360))

    if h:
        generated_hpr.x = h
    if p:
        generated_hpr.y = p
    if r:
        generated_hpr.z = r

    return generated_hpr
