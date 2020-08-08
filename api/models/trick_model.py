import json


class TrickModel:
    """"
        uid - Unique ID generated for trick
        name - trick's name
        discipline - name's of discipline trick belongs to
        category - trick's category i.e. 'aerial', 'jump', 'wave' ...
        tutorials - array of videos' URL containing trick's tutorials
        videos - array of videos' URL containing trick's video showdown
    """

    def __init__(self, uid: str, name: str, discipline: str, category: str, tutorials: [str], videos: [str]):
        self.uid = uid
        self.name = name
        self.discipline = discipline
        self.category = category
        self.tutorials = tutorials
        self.videos = videos

    def to_json(self):
        return json.loads(json.dumps(self, default=lambda o: o.__dict__,
                                     sort_keys=False, indent=4))
