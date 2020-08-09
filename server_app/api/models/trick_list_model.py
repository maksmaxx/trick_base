import json
from api.models.trick_model import TrickModel


class TrickListModel:
    """"
        tricks - Array with TrickModel objects
    """

    def __init__(self, tricks: [TrickModel]):
        self.tricks = tricks

    def to_json(self):
        return json.loads(json.dumps(self, default=lambda o: o.__dict__,
                                     sort_keys=False, indent=4))
