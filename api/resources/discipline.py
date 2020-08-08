from flask_restful import Resource, reqparse
from services.mongo_client import MongoClient
from models.discipline_model import DisciplineModel


class Discipline(Resource):
    def get(self, name):
        # Connect to DB
        client = MongoClient()
        if client.connect():
            # Find discipline with name
            discipline = client.find_discipline_with_name(name)
            if discipline is not None:
                return discipline.to_json(), 200
            else:
                return "Discipline not found", 404
        # Connection to DB error
        else:
            return "Service temporary unavailable", 503

    def put(self, name):
        # Process JSON income
        incoming = self.__process_arguments(name)
        if incoming is not None:
            # Connect to DB
            client = MongoClient()
            if client.connect():
                # Check if discipline already exists
                # Exists, update old discipline
                if client.find_discipline_with_name(incoming.name) is not None:
                    result = client.update_discipline(incoming)
                    if result is not None:
                        return result.to_json(), 200
                    # Update error
                    else:
                        return "Update error", 400

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

    def delete(self, name):
        # Connect to DB
        client = MongoClient()
        if client.connect():
            if client.delete_discipline(name):
                return "Discipline deleted", 200
            else:
                return "Deletion error", 400
        # Connection to DB error
        else:
            return "Service temporary unavailable", 503


    def __process_arguments(self, name):
        # Validate parameters provided with JSON
        # Returns None if error, DisciplineModel if success
        try:
            parser = reqparse.RequestParser()
            parser.add_argument("area")
            parser.add_argument("image")
            params = parser.parse_args()

            # Parameters must not be null
            if params["image"] is None or params["area"] is None or name is None:
                raise

            return DisciplineModel(
                image=params["image"],
                area=params["area"],
                name=str(name),
            )

        except Exception as e:
            print(e)
            return None
