from panda3d.core import GeomVertexFormat, GeomVertexData
from panda3d.core import Geom, GeomTriangles, GeomVertexWriter
from panda3d.core import GeomNode
from panda3d.core import LVector3, LVector4f
from direct.interval.LerpInterval import LerpHprInterval
import random
from config.Config import rotate_time
from src.utility.Functions import get_random_hpr, get_random_position
from src.utility.Color import Color
from src.objects.Object import Object, ObjectType


def normalized(*args):
    my_vec = LVector3(*args)
    my_vec.normalize()
    return my_vec


class Cube(Object):
    cube = None

    def __init__(self, _renderer, _loader, _debugger, scale=1, _color=LVector4f(0.0, 0.0, 0.0, 0.0)):
        Object.__init__(self, _renderer, _loader, _debugger, _type=ObjectType.CUBE, _hpr=get_random_hpr())
        self.color = _color
        self.square0 = self.make_square(-1*scale, -1*scale, -1*scale,
                                        1*scale, -1*scale, 1*scale)
        self.square1 = self.make_square(-1*scale, 1*scale, -1*scale,
                                        1*scale, 1*scale, 1*scale)
        self.square2 = self.make_square(-1*scale, 1*scale, 1*scale,
                                        1*scale, -1*scale, 1*scale)
        self.square3 = self.make_square(-1*scale, 1*scale, -1*scale,
                                        1*scale, -1*scale, -1*scale)
        self.square4 = self.make_square(-1*scale, -1*scale, -1*scale,
                                        -1*scale, 1*scale, 1*scale)
        self.square5 = self.make_square(1*scale, -1*scale, -1*scale,
                                        1*scale, 1*scale, 1*scale)

        self.node = GeomNode('square')
        self.node.addGeom(self.square0)
        self.node.addGeom(self.square1)
        self.node.addGeom(self.square2)
        self.node.addGeom(self.square3)
        self.node.addGeom(self.square4)
        self.node.addGeom(self.square5)

        self.intervals = []

        if self.render:
            self.render_object()
            self.rotate()

    def generate(self):
        self.rendered_object.setPos(get_random_position(y=3))
        self.rendered_object.setHpr(self.hpr)

    def delete(self):
        for interval in self.intervals:
            interval.finish()
        self.intervals = []
        self.rendered_object.removeNode()

    def get_pos(self):
        return self.rendered_object.node

    def make_square(self, x1, y1, z1, x2, y2, z2):
        # https://github.com/panda3d/panda3d/blob/master/samples/procedural-cube/main.py
        format = GeomVertexFormat.getV3n3c4()
        vdata = GeomVertexData('square', format, Geom.UHDynamic)

        vertex = GeomVertexWriter(vdata, 'vertex')
        normal = GeomVertexWriter(vdata, 'normal')
        color_writer = GeomVertexWriter(vdata, 'color')

        # make sure we draw the square in the right plane
        if x1 != x2:
            vertex.addData3(x1, y1, z1)
            vertex.addData3(x2, y1, z1)
            vertex.addData3(x2, y2, z2)
            vertex.addData3(x1, y2, z2)

            normal.addData3(normalized(2 * x1 - 1, 2 * y1 - 1, 2 * z1 - 1))
            normal.addData3(normalized(2 * x2 - 1, 2 * y1 - 1, 2 * z1 - 1))
            normal.addData3(normalized(2 * x2 - 1, 2 * y2 - 1, 2 * z2 - 1))
            normal.addData3(normalized(2 * x1 - 1, 2 * y2 - 1, 2 * z2 - 1))
        else:
            vertex.addData3(x1, y1, z1)
            vertex.addData3(x2, y2, z1)
            vertex.addData3(x2, y2, z2)
            vertex.addData3(x1, y1, z2)

            normal.addData3(normalized(2 * x1 - 1, 2 * y1 - 1, 2 * z1 - 1))
            normal.addData3(normalized(2 * x2 - 1, 2 * y2 - 1, 2 * z1 - 1))
            normal.addData3(normalized(2 * x2 - 1, 2 * y2 - 1, 2 * z2 - 1))
            normal.addData3(normalized(2 * x1 - 1, 2 * y1 - 1, 2 * z2 - 1))

        for i in range(0, 4):
            random_color = self.color.get_color()
            if type(random_color) != Color:
                raise Exception("random_color is NOT a Color: " + str(type(random_color)))
            color_writer.addData4f(random_color.x, random_color.y, random_color.z, random_color.getW())

        tris = GeomTriangles(Geom.UHStatic)
        tris.addVertices(0, 1, 3)
        tris.addVertices(1, 2, 3)

        square = Geom(vdata)
        square.addPrimitive(tris)
        return square

    def rotate(self):
        multiplicities = [1, -1]

        if self.rendered_object:
            cur_hpr = self.rendered_object.getHpr()
            new_hpr = (cur_hpr.x + (360 * random.choice(multiplicities)),
                       cur_hpr.y + (360 * random.choice(multiplicities)),
                       cur_hpr.z + (360 * random.choice(multiplicities)))
            first_interval = LerpHprInterval(self.rendered_object, rotate_time, new_hpr)

            self.intervals.append(first_interval)

            first_interval.loop()
        else:
            raise Exception("No self.cube to rotate!")
