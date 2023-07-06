from enum import Enum
from direct.gui.OnscreenImage import OnscreenImage
from panda3d.core import TransparencyAttrib
from src.utility.Color import ColorGroup, Color


image_directory = "img/"
file_extension = ".png"


class TYPES(Enum):
    BASE = "base"
    SHADE = "shade"
    LINE = "line"


class Part(OnscreenImage):
    def __init__(self, _loader, _debugger, _variant, _type, _pupil=False, _closed=False, _id=None, _object_id=0):
        self.debugger = _debugger
        self.variant = _variant
        self.type = _type
        self.pupil = _pupil
        self.closed = _closed
        self.object_id = _object_id

        if _id:
            self.object_id = _id

        self.texture = _loader.loadTexture(self.get_file_name())

        OnscreenImage.__init__(self, image=self.texture, pos=(-0.05, 0, 0.02), scale=0.5)
        self.setTransparency(TransparencyAttrib.MAlpha)

    def get_file_name(self):
        if self.pupil:
            return image_directory + str(self.variant) + " pupil " + self.type.value + file_extension
        elif self.closed:
            return image_directory + str(self.variant) + " " + self.type.value + " closed" + file_extension
        else:
            return image_directory + str(self.variant) + " " + self.type.value + file_extension

    def __str__(self):
        return f"Object {str(self.object_id)} Part {self.type.value} Pupil {str(self.pupil)} Closed {str(self.closed)}"

    def destroy(self):
        OnscreenImage.destroy(self)
        self.debugger = None
        self.variant = None
        self.type = None
        self.pupil = None
        self.texture = None

    def tint_image(self, _color):
        if self.node:
            if type(_color) == ColorGroup:
                self.setColor(_color.get_color())
            elif type(_color) == Color:
                self.setColor(_color)
            else:
                raise Exception("Part | Wrong _color type: " + str(type(_color)))
        else:
            raise Exception("Part | No node to tint!")
