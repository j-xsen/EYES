from enum import Enum

from panda3d.core import LVector3, CullFaceAttrib


class ObjectType(Enum):
    CUBE = 0,
    EYE = 1


class Object:
    intervals = []
    sequences = []

    def __init__(self, _renderer, _loader, _debugger, _type, _pos=LVector3(0, 0, 0), _hpr=LVector3(0, 0, 0), _scale=1,
                 _object_id=0):
        self.render = _renderer
        self.debugger = _debugger
        self.loader = _loader
        self.type = _type
        self.pos = _pos
        self.hpr = _hpr
        self.scale = _scale
        self.rendered_object = None
        self.object_id = _object_id

    def __str__(self):
        if self.type == ObjectType.EYE:
            return "Eye"
        elif self.type == ObjectType.CUBE:
            return "Cube"

    def give_id(self, _id):
        self.object_id = _id

    def delete(self):
        self.intervals = None
        self.sequences = None
        self.render = None
        self.debugger = None
        self.loader = None
        self.type = None
        self.pos = None
        self.hpr = None
        self.scale = None
        if self.rendered_object:
            self.rendered_object.clear()
        self.rendered_object = None

    def render_object(self):
        self.rendered_object = self.render.attachNewNode(self.node)
        self.rendered_object.setAttrib(CullFaceAttrib.make(CullFaceAttrib.MCullNone))

    def set_hpr(self, hpr):
        self.rendered_object.setHpr(hpr)

    def set_pos(self, pos):
        self.rendered_object.setPos(pos)

    def generate(self):
        raise Exception("Need to overwrite a Object.generate")
        pass
