from flask_restful import Resource, reqparse

from services.mongo_client import MongoClient
from models.discipline_model import DisciplineModel
import protected.const as protected  # Paths to DB, passwords, not included in git


class Discipline(Resource):
    """
    Discipline provides endpoints:
    GET 	/api/discipline/{name} : Get the discipline identified by "name"
    PUT 	/api/discipline/{name} : Update the discipline identified by "name"
    DELETE	/api/discipline/{name} : Delete the discipline identified by "name"(and all associated tricks)
    """

    def get(self, name):
        """
        GET 	/api/discipline/{name} : Get the discipline identified by "name"

        GET Json structure:
        {
            "name": "<name>",
            "area": "<area>",
            "image": "<image_path>"
        }
        """

        client = MongoClient()
        if client.connect():
            discipline = client.find_discipline_with_name(name)
            if discipline is not None:
                return discipline.to_json(), 200
            else:
                return "Discipline not found", 404
        # Connection to DB error
        else:
            return "Service temporary unavailable", 503

    def put(self, name):
        """
        PUT 	/api/discipline/{name} : Update the discipline identified by "name"

        PUT Json structure:
        {
            "key": "<authorization_key>",
            "area": "<area>",
            "image": "<image_path>"
        }
        """

        incoming = self.__process_arguments(name)
        if isinstance(incoming, DisciplineModel):
            client = MongoClient()
            if client.connect():
                # Check if discipline already exists
                # Exists, update old discipline
                if client.find_discipline_with_name(incoming.name) is not None:
                    result = client.update_discipline(incoming)
                    if result is not None:
                        return result.to_json(), 200
                    else:
                        return "Update error", 400

                # Not exists, abort
                else:
                    return "Can't update. Discipline not exists.", 400

            # Connection to DB error
            else:
                return "Service temporary unavailable", 503
        elif incoming == "unauthorized":
            return "Unauthorized", 401
        # Incorrect incoming JSON parameters
        else:
            return "Invalid discipline parameters", 400

    def delete(self, name):
        """
        DELETE	/api/discipline/{name} : Delete the discipline identified by "name"(and all associated tricks)

        DELETE Json structure
        {
            "key": "key"
        }
        """

        # Check if user is authorized to PUT/POST/DELETE
        try:
            parser = reqparse.RequestParser()
            parser.add_argument("key")
            params = parser.parse_args()

            if params["key"] != protected.AUTHKEY:
                return "Unauthorized", 401
        except Exception as e:
            print(e)

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
            parser.add_argument("key")
            parser.add_argument("area")
            parser.add_argument("image")
            params = parser.parse_args()

            # Parameters must not be null
            if params["image"] is None or params["area"] is None or name is None:
                raise

            # Check if user is authorized to PUT/POST/DELETE
            if params["key"] != protected.AUTHKEY:
                return "unauthorized"

            return DisciplineModel(
                image=params["image"],
                area=params["area"],
                name=str(name),
            )

        except Exception as e:
            print(e)
            return None
