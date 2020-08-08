import json
from models.discipline_model import DisciplineModel


class DisciplineListModel:
    """"
        disciplines - Array with DisciplineModel objects
    """
    def __init__(self, disciplines: [DisciplineModel]):
        self.disciplines = disciplines

    def to_json(self):
        return json.loads(json.dumps(self, default=lambda o: o.__dict__,
                                     sort_keys=False, indent=4))
