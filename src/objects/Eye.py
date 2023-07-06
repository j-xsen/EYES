from src.objects.Part import Part, TYPES
from direct.interval.LerpInterval import LerpHprInterval, LerpScaleInterval
from direct.interval.IntervalGlobal import Sequence, Func, Wait
from src.utility.Functions import *
from src.objects.Object import Object, ObjectType


class Eye(Object):
    parts = None
    open = False

    def __init__(self, _renderer, _loader, _debugger, _variant, _color, _pos, _skin_color, _object_id):
        Object.__init__(self, _renderer, _loader, _debugger, _type=ObjectType.EYE, _pos=_pos, _hpr=get_random_hpr(),
                        _object_id=_object_id)
        self.variant = _variant
        self.generate_eye()
        self.change_eye_color(_color)
        self.change_skin_color(_skin_color)
        self.put_in_specific_position()
        blink_interval = Func(self.blink)
        loop_blink_sequence = Sequence(blink_interval, Wait(1))
        loop_blink_sequence.loop()
        self.intervals.append(blink_interval)
        self.sequences.append(loop_blink_sequence)
        self.rotate()

    def __str__(self):
        return "Eye " + str(self.variant)

    def generate_eye(self):
        self.scale = random.randint(1, 25) / 100
        base = Part(self.loader, self.debugger, self.variant, TYPES.BASE,
                    _object_id=self.object_id)
        base_closed = Part(self.loader, self.debugger, self.variant, TYPES.BASE, _closed=True,
                           _object_id=self.object_id)
        pupil_base = Part(self.loader, self.debugger, self.variant, TYPES.BASE, _pupil=True,
                          _object_id=self.object_id)
        pupil_shade = Part(self.loader, self.debugger, self.variant, TYPES.SHADE, _pupil=True,
                           _object_id=self.object_id)
        line = Part(self.loader, self.debugger, self.variant, TYPES.LINE,
                    _object_id=self.object_id)
        line_closed = Part(self.loader, self.debugger, self.variant, TYPES.LINE, _closed=True,
                           _object_id=self.object_id)
        self.parts = {
            "base": base,
            "base_closed": base_closed,
            "pupil_base": pupil_base,
            "pupil_shade": pupil_shade,
            "line": line,
            "line_closed": line_closed,
        }
        self.open_eye()

    def delete(self):
        Object.delete(self)
        for part, value in self.parts.items():
            value.destroy()
            self.parts[part] = None
        self.variant = None
        self.parts = None

    def change_eye_color(self, _color):
        self.parts["pupil_base"].tint_image(_color)

    def change_skin_color(self, _color):
        self.parts["base_closed"].tint_image(_color)

    def put_in_random_position(self):
        if not self.parts:
            raise Exception("No nodes defined for " + str(self))

        self.pos = get_random_position()
        self.hpr = get_random_hpr()

        self.put_in_specific_position()

    def put_in_specific_position(self):
        for name, obj in self.parts.items():
            obj.setPos(self.pos)
            obj.setScale(self.scale)
            obj.setHpr(self.hpr)

    def close_eye(self):
        for name, obj in self.parts.items():
            if not obj.closed:
                obj.hide()
            else:
                obj.show()
        self.open = False

    def open_eye(self):
        for name, obj in self.parts.items():
            if obj.closed:
                obj.hide()
            else:
                obj.show()
        self.open = True

    def rotate(self):
        rotate_table = [0, 1, 1, 1, 1, 1, 1, -1, -1, -1, 0, 0, -1, -1, 1, 1, -1]
        rotate_axis = LVector3(random.choice(rotate_table), random.choice(rotate_table), random.choice(rotate_table))
        random_scale = (random.randint(1, 25) / 100) + 1
        for name, obj in self.parts.items():
            cur_hpr = obj.getHpr()
            new_hpr = LVector3(cur_hpr.x + 360 * rotate_axis.x,
                               cur_hpr.y + 360 * rotate_axis.y,
                               cur_hpr.z + 360 * rotate_axis.z)
            new_hpr_interval = LerpHprInterval(obj, rotate_time, new_hpr,
                                               name=f"Eye HPR Interval {str(obj)}")
            grow_scale_interval = LerpScaleInterval(obj, rotate_time, self.scale * random_scale,
                                                    name=f"Eye Grow Scale Interval {str(obj)}")
            shrink_scale_interval = LerpScaleInterval(obj, rotate_time, self.scale,
                                                      name=f"Eye Shrink Scale Interval {str(obj)}")
            scale_sequence = Sequence(grow_scale_interval, shrink_scale_interval,
                                      name=f"Eye Sequence {str(obj)}")
            new_hpr_interval.loop()
            scale_sequence.loop()
            self.intervals.append(new_hpr_interval)
            self.intervals.append(grow_scale_interval)
            self.intervals.append(shrink_scale_interval)
            self.sequences.append(scale_sequence)

    def blink(self):
        if not self.render:
            return
        if not self.open:
            self.open_eye()
            return
        if random.randint(1, 696969) <= 4200:
            self.close_eye()
        return
