import json


class DisciplineListModel:
    def __init__(self, disciplines: []):
        self.disciplines = disciplines

    def to_json(self):
        return json.loads(json.dumps(self, default=lambda o: o.__dict__,
                                     sort_keys=False, indent=4))
