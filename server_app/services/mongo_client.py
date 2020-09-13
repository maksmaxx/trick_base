import pymongo
import pymongo.results
from api.models.discipline_model import DisciplineModel
from api.models.discipline_list_model import DisciplineListModel
from api.models.trick_model import TrickModel
from api.models.trick_list_model import TrickListModel


class MongoClient:
    """
    Provides methods to interact with data stored in MongoDB's Cluster
    """

    def __init__(self):
        self.client = None
        self.database = None
        self.MONGO_PATH = "mongodb+srv://heroku_app:F1p5ouXuIN6nbMya@cluster0.cfpoc.mongodb.net/trick_base?retryWrites=true&w=majority"

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

    def find_all_disciplines(self):
        """
        Searches for all disciplines in existed in collection
        :return: DisciplineListModel
        """
        collection = pymongo.collection.Collection(self.database, 'disciplines')
        cursor = collection.find({})

        lst = []
        for document in cursor:
            lst.append(
                DisciplineModel(
                    name=document["name"],
                    area=document["area"],
                )
            )

        return DisciplineListModel(disciplines=lst)

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
                videos=result["videos"]
            )

    def find_all_tricks(self):
        """
        Find all tricks in DB
        :return: TrickListModel
        """

        collection = pymongo.collection.Collection(self.database, 'tricks')
        result = collection.find({})

        lst = []
        for document in result:
            lst.append(TrickModel(
                uuid=document["uuid"],
                name=document["name"],
                discipline=document["discipline"],
                videos=document["videos"]
            ))

        return TrickListModel(tricks=lst)

    def find_all_tricks_belonging_to(self, discipline: str):
        """
        Find discipline's tricks
        Returns TrickListModel
        """
        collection = pymongo.collection.Collection(self.database, 'tricks')
        result = collection.find({"discipline": discipline})

        lst = []
        for document in result:
            lst.append(TrickModel(
                uuid=document["uuid"],
                name=document["name"],
                discipline=document["discipline"],
                videos=document["videos"]
            ))

        return TrickListModel(tricks=lst)

