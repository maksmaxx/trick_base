import pymongo
import pymongo.results
from api.models.discipline_model import DisciplineModel
from api.models.discipline_list_model import DisciplineListModel
from api.models.trick_model import TrickModel
from api.models.trick_list_model import TrickListModel
import protected.const as protected  # Paths to DB, passwords, not included in git


class MongoClient:
    """
    Provides methods to interact with data stored in MongoDB
    """

    def __init__(self):
        self.client = None
        self.database = None

    def connect(self):
        """
        Connects to default mongoDB cluster, path is private and stored
        in protected/const.py => MONGOPATH = "<path_to_mongo_cluster>"
        """
        try:
            self.client = pymongo.MongoClient(protected.MONGOPATH)
            self.database = self.client.get_database()
            return True

        except Exception as e:
            print(e)
            return False

    def find_all_disciplines(self):
        """
        Searches for all disciplines in existed in collection
        Returns DisciplineList
        """
        collection = pymongo.collection.Collection(self.database, 'disciplines')
        cursor = collection.find({})

        lst = []
        for document in cursor:
            lst.append(
                DisciplineModel(
                    name=document["name"],
                    area=document["area"],
                    image=document["image"]
                )
            )

        return DisciplineListModel(disciplines=lst)

    def find_discipline_with_name(self, name: str):
        """
        Searches for discipline with provided name
        Returns DisciplineModel or None if not exists
        """

        collection = pymongo.collection.Collection(self.database, 'disciplines')
        result = collection.find_one({"name": name})

        if result is None:
            return None
        else:
            return DisciplineModel(
                name=result["name"],
                area=result["area"],
                image=result["image"]
            )

    def create_discipline(self, discipline: DisciplineModel):
        """
        Creates discipline in DB
        Returns created discipline or None if failed
        """

        collection = pymongo.collection.Collection(self.database, 'disciplines')
        count = collection.count_documents(discipline.to_json())

        if count == 0:
            collection.insert_one(discipline.to_json())
            return discipline
        elif count > 0:
            return None

    def update_discipline(self, discipline: DisciplineModel):
        """
        Update discipline in DB
        Returns updated discipline or None if failed
        Name cannot be CHANGED
        """

        collection = pymongo.collection.Collection(self.database, 'disciplines')

        try:
            collection.find_one_and_replace({"name": discipline.name}, discipline.to_json())
            return discipline
        except Exception as e:
            print(e)
            return None

    def delete_discipline(self, name: str):
        """
        Delete discipline in DB
        Delete all discipline's associated tricks
        Returns True or False
        """

        self.delete_all_tricks_associated_with_discipline(name)
        collection = pymongo.collection.Collection(self.database, 'disciplines')
        result = collection.delete_one({"name": name})

        if result.deleted_count > 0:
            return True
        else:
            return False

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
                category=document["category"],
                videos=document["videos"]
            ))

        return TrickListModel(tricks=lst)

    def create_trick(self, trick: TrickModel):
        """
        Creates trick in DB
        Returns created trick or None if failed
        """

        collection = pymongo.collection.Collection(self.database, 'tricks')
        count = collection.count_documents(trick.to_json())

        if count == 0:
            collection.insert_one(trick.to_json())
            return trick
        elif count > 0:
            return None

    def update_trick(self, trick: TrickModel):
        """
        Update trick in DB
        Returns updated trick or None if failed
        """
        collection = pymongo.collection.Collection(self.database, 'tricks')

        try:
            collection.find_one_and_replace({"uuid": trick.uuid}, trick.to_json())
            return trick
        except Exception as e:
            print(e)
            return None

    def delete_trick(self, uuid: str):
        """
        Delete trick in DB
        Returns True or False
        """

        collection = pymongo.collection.Collection(self.database, 'tricks')
        result = collection.delete_one({"uuid": uuid})

        if result.deleted_count > 0:
            return True
        else:
            return False

    def delete_all_tricks_associated_with_discipline(self, name: str):
        """
        Deletes all tricks having discipline's name saved
        """

        collection = pymongo.collection.Collection(self.database, 'tricks')
        collection.delete_many({"discipline": name})
