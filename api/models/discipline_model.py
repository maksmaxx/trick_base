import json


class DisciplineModel:
    def __init__(self, name, area, image):
        self.name = name
        self.area = area
        self.image = image

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
