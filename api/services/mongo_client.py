import pymongo
import pymongo.results
from models.discipline_model import DisciplineModel
from models.discipline_list_model import DisciplineListModel
import protected.const as protected  # Paths to DB, passwords, not included in git


class MongoClient:
    def __init__(self):
        self.client = None
        self.database = None

    def connect(self):
        # Connect to default mongoDB cluster
        try:
            self.client = pymongo.MongoClient(protected.MONGOPATH)
            self.database = self.client.get_database()
            return True

        except Exception as e:
            print(e)
            return False

    def find_all_disciplines(self):
        # Searches for all disciplines in collection
        # Returns DisciplineList
        collection = pymongo.collection.Collection(self.database, 'disciplines')
        cursor = collection.find({})

        list = []
        for document in cursor:
            list.append(
                DisciplineModel(
                    name=document["name"],
                    area=document["area"],
                    image=document["image"]
                )
            )

        return DisciplineListModel(disciplines=list)

    def find_discipline_with_name(self, name: str):
        # Searches for discipline with provided name
        # Returns DisciplineModel from DB or None if not exists

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
        # Creates discipline in DB
        # Returns created discipline or None if failed

        collection = pymongo.collection.Collection(self.database, 'disciplines')
        count = collection.count_documents(discipline.to_json())

        if count == 0:
            collection.insert_one(discipline.to_json())
            return discipline
        elif count > 0:
            return None

    def update_discipline(self, discipline: DisciplineModel):
        # Update discipline in DB
        # Returns updated discipline or None if failed

        collection = pymongo.collection.Collection(self.database, 'disciplines')

        try:
            collection.find_one_and_replace({"name": discipline.name}, discipline.to_json())
            return discipline
        except Exception as e:
            print(e)
            return None

    def delete_discipline(self, name):
        # Delete discipline in DB
        # Returns True or False

        collection = pymongo.collection.Collection(self.database, 'disciplines')
        result = collection.delete_one({"name": name})

        if result.deleted_count > 0:
            return True
        else:
            return False
