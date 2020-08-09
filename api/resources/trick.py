from flask_restful import Resource, reqparse

from services.mongo_client import MongoClient
from models.trick_model import TrickModel
import protected.const as protected  # Paths to DB, passwords, not included in git


class Trick(Resource):
    """
    Trick provides endpoints:
    GET     /api/trick/{uuid} : Get the trick identified by "id"
    PUT     /api/trick/{uuid} : Update the trick identified by "id"
    DELETE  /api/trick/{uuid} : Delete the trick identified by "id"
    """

    def get(self, uuid):
        """
        GET     /api/trick/{uuid} : Get the trick identified by "id"

        GET Json structure:
        {
            "uid": "<uuid>",
            "name": "<trick_name>",
            "discipline": "<discipline_name>",
            "category": "<discipline_trick_category_name>",
            "videos": [
                "<URL to trick's video 1>",
                "<URL to trick's video 2>",
                "<URL to ...>"
            ]
        }
        """

        client = MongoClient()
        if client.connect():
            trick = client.find_trick_with_uuid(uuid)
            if trick is not None:
                return trick.to_json(), 200
            else:
                return "Trick not found", 404
        # Connection to DB error
        else:
            return "Service temporary unavailable", 503

    def put(self, uuid):
        """
        PUT     /api/trick/{uuid} : Update the trick identified by "id"
        Trick must exists!

        PUT Json structure:
        {
            "key": "<authorization_key>",~`
            "name": "<trick_name>",
            "discipline": "<discipline_name>",
            "category": "<discipline_trick_category_name>",
            "videos": [
                "<URL to trick's video 1>",
                "<URL to trick's video 2>",
                "<URL to ...>"
            ]
        }
        """

        incoming: TrickModel = self.__process_arguments(uuid)
        if isinstance(incoming, TrickModel):
            client = MongoClient()
            if client.connect():
                # If exists, update trick
                if client.find_trick_with_uuid(uuid) is not None:
                    if client.find_discipline_with_name(incoming.discipline) is not None:
                        result = client.update_trick(incoming)
                        if result is not None:
                            return result.to_json(), 200
                        else:
                            return "Update error", 400
                    else:
                        return "Can't update. Discipline not exists.", 400
                else:
                    return "Can't update. Trick not exists.", 400

            # Connection to DB error
            else:
                return "Service temporary unavailable", 503

        elif incoming == "unauthorized":
            return "Unauthorized.", 401
        # Incorrect incoming JSON parameters
        else:
            return "Invalid trick parameters", 400

    def delete(self, uuid):
        """
        DELETE  /api/trick/{uuid} : Delete the trick identified by "uid"

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
            if client.delete_trick(uuid):
                return "Trick deleted", 200
            else:
                return "Deletion error", 400
        # Connection to DB error
        else:
            return "Service temporary unavailable", 503

    def __process_arguments(self, uuid):
        """
        Validate parameters provided with JSON
        Returns None if error in data, TrickModel otherwise
        """

        try:
            parser = reqparse.RequestParser()
            parser.add_argument("key")
            parser.add_argument("name")
            parser.add_argument("discipline")
            parser.add_argument("category")
            parser.add_argument("videos", action='append')
            params = parser.parse_args()

            # Parameters must not be null
            if params["name"] is None or params["category"] is None or params["videos"] is None\
                    or params["discipline"] is None:
                raise

            # Check if user is authorized to PUT/POST/DELETE
            if params["key"] != protected.AUTHKEY:
                return "unauthorized"

            return TrickModel(
                uuid=str(uuid),
                name=params["name"],
                discipline=params["discipline"],
                category=params["category"],
                videos=params["videos"]
            )

        except Exception as e:
            print(e)
            return None
