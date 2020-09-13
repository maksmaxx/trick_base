import pymongo
import pymongo.results
from models.discipline_model import DisciplineModel
from models.trick_model import TrickModel
import uuid


class MongoClient:
    """
    Provides methods to interact with data stored in MongoDB's Cluster
    """

    def __init__(self, path: str):
        self.client = None
        self.database = None
        self.MONGO_PATH = path

    def connect(self):
        """
        Connects to default mongoDB cluster
        """
        try:
            self.client = pymongo.MongoClient(self.MONGO_PATH)
            self.database = self.client.get_database()
            return True

        except Exception as e:
            print(e)
            return False

    def find_discipline_with_name(self, name: str):
        """
        Searches for discipline with provided name
        :returns: DisciplineModel or None
        """

        collection = pymongo.collection.Collection(self.database, 'disciplines')
        result = collection.find_one({"name": name})

        if result is None:
            return None
        else:
            return DisciplineModel(
                name=result["name"],
                area=result["area"],
            )

    def find_trick_with_uuid(self, uuid: str):
        """
        Find trick with given UUID in DB
        Returns TrickModel or None
        """

        collection = pymongo.collection.Collection(self.database, 'tricks')
        result = collection.find_one({"uuid": uuid})

        if result is None:
            return None
        else:
            return TrickModel(
                uuid=result["uuid"],
                name=result["name"],
                discipline=result["discipline"],
                category=result["category"],
                videos=result["videos"]
            )

    def create_discipline(self, name: str, area: str):
        collection = pymongo.collection.Collection(self.database, 'disciplines')
        result = self.find_discipline_with_name(name=name)
        if result is None:
            try:
                collection.insert_one(DisciplineModel(
                    name=name,
                    area=area,
                ).to_json())
                return "Discipline created"
            except Exception as e:
                print(e)
                return "DB error"
        else:
            return "Discipline already exists"

    def create_trick(self, name: str, discipline: str, category: str, videos):
        collection = pymongo.collection.Collection(self.database, 'tricks')
        result = self.find_discipline_with_name(discipline)
        if result is not None:
            try:
                collection.insert_one(
                    TrickModel(
                        uuid=str(uuid.uuid1()),
                        name=name,
                        discipline=discipline,
                        category=category,
                        videos=videos
                    ).to_json())
                return "Trick created"
            except Exception as e:
                print(e)
                return "DB error"
        else:
            return "Provided discipline not exists"

    def delete_trick(self, u_id: str):
        collection = pymongo.collection.Collection(self.database, 'tricks')
        result = self.find_trick_with_uuid(u_id)
        if result is not None:
            try:
                collection.delete_one({"uuid": u_id})
                return "Trick deleted"
            except Exception as e:
                print(e)
                return "DB error"
        else:
            return "Trick not exists"
