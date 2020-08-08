from flask_restful import Resource, reqparse
from services.mongo_client import MongoClient
from models.discipline_list_model import DisciplineListModel
from models.discipline_model import DisciplineModel


class DisciplineList(Resource):
    def get(self):
        # Connect to DB
        client = MongoClient()
        if client.connect():
            result: DisciplineListModel = client.find_all_disciplines()
            return result.to_json(), 200

        # Connection to DB error
        else:
            return "Service temporary unavailable", 503

    def post(self):
        # Process JSON income
        incoming = self.__process_arguments()

        if incoming is not None:
            # Connect to DB
            client = MongoClient()
            if client.connect():
                # Check if discipline already exists
                # Exists, operation not allowed
                if client.find_discipline_with_name(incoming.name) is not None:
                    return "Already exists", 400
                # Not exists, create new discipline
                else:
                    result = client.create_discipline(incoming)
                    if result is not None:
                        return result.to_json(), 201
                    # Creation error
                    else:
                        return "Already exists", 400

            # Connection to DB error
            else:
                return "Service temporary unavailable", 503
        # Incorrect incoming JSON parameters
        else:
            return "Invalid discipline parameters", 400

    def __process_arguments(self):
        # Validate parameters provided with JSON
        # Returns None if error, DisciplineModel if success
        try:
            parser = reqparse.RequestParser()
            parser.add_argument("name")
            parser.add_argument("area")
            parser.add_argument("image")
            params = parser.parse_args()

            # Parameters must not be null
            if params["image"] is None or params["area"] is None or params["name"] is None:
                raise

            return DisciplineModel(
                image=params["image"],
                area=params["area"],
                name=params["name"],
            )

        except Exception as e:
            print(e)
            return None
