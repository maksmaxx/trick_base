import json


class DisciplineModel:
    """"
        name - Unique name chosen for discipline
        area - i.e. land, water, snow ...
        image - path to valid image to display for clients
    """
    def __init__(self, name: str, area: str, image: str):
        self.name = name
        self.area = area
        self.image = image

    def to_json(self):
        return json.loads(json.dumps(self, default=lambda o: o.__dict__,
                                     sort_keys=False, indent=4))
