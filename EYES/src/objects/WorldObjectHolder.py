# WO(a)H


class WorldObjectHolder:
    def __init__(self, _chosen_map, _object_type):
        self.chosen_map = _chosen_map
        self.object_type = _object_type
        self.objects = []

    def add_object(self, _object):
        if _object.type == self.object_type:
            _object.give_id(len(self.objects))
            self.objects.append(_object)
        else:
            raise Exception(f"WorldObjectHolder | Tried adding {str(type(_object.type))} to {self.object_type}")

    def num_objects(self):
        return len(self.objects)

    def destroy(self):
        for i in range(len(self.objects)):
            self.objects[i].delete()
            self.objects[i] = None
        self.object_type = None
        self.chosen_map = None
        self.objects = None
