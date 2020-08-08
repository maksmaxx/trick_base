class DisciplineModel:
    def __init__(self, name: str, area: str, image: str):
        self.name = name
        self.area = area
        self.image = image

    def to_json(self):
        return {
            "name": self.name,
            "area": self.area,
            "image": self.image
        }

        # return json.dumps(self, default=lambda o: o.__dict__,
        #                 sort_keys=True, indent=4)
