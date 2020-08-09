import uuid
from flask_restful import Resource, reqparse

from services.mongo_client import MongoClient
from models.trick_model import TrickModel
from models.trick_list_model import TrickListModel
import protected.const as protected


class TrickList(Resource):
    """
    TrickList provides endpoints:
    GET     /api/tricks/{discipline_name} : Get all tricks belonging to discipline identified by "discipline_name"
    POST    /api/tricks/{discipline_name} : Create a new trick belonging to discipline identified by "discipline_name"
    """

    def get(self, discipline):
        """
        GET     /api/tricks/{discipline_name} : Get all tricks belonging to discipline identified by "discipline_name"
        Discipline needs to be in DB. Abort operation otherwise(no discipline == no tricks)

        GET Json structure:
        {
            "tricks": [
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
                },
                { NEXT TRICKS }... ,
            ]
        }
        """

        client = MongoClient()
        if client.connect():
            # Check if discipline name is provided
            if client.find_discipline_with_name(discipline) is not None:
                result: TrickListModel = client.find_all_tricks_belonging_to(discipline)
                return result.to_json(), 200
            else:
                return "Discipline not found", 404

        # Connection to MongoDB error
        else:
            return "Service temporary unavailable", 503

    def post(self, discipline):
        """
        POST    /api/tricks/{discipline_name} : Create a new trick
                belonging to discipline identified by "discipline_name"

        Discipline and category need to exists! Abort otherwise.

        POST Json structure:
            {
                "key": "<authorization_key>",
                "name": "<trick_name>",
                "category": "<discipline_trick_category_name>",
                "videos": [
                    "<URL to trick's video 1>",
                    "<URL to trick's video 2>",
                    "<URL to ...>"
                ]
            }
        """

        # Process JSON income
        incoming = self.__process_arguments(discipline)
        if isinstance(incoming, TrickModel):
            client = MongoClient()
            if client.connect():
                # Check if provided discipline exists
                if client.find_discipline_with_name(incoming.discipline) is not None:
                    result = client.create_trick(incoming)
                    if result is not None:
                        return result.to_json(), 201
                    else:
                        return "Already exists", 400
                else:
                    return "Discipline not exists. Provide valid discipline or create new one to add trick.", 400

            # Connection to MongoDB error
            else:
                return "Service temporary unavailable", 503

        elif incoming == "unauthorized":
            return "Unauthorized.", 401
        # Incorrect incoming JSON parameters
        else:
            return "Invalid discipline parameters or authorization key.", 400

    def __process_arguments(self, discipline):
        """
        Validate parameters provided with JSON
        Returns None if error in data, TrickModel otherwise
        """

        try:
            parser = reqparse.RequestParser()
            parser.add_argument("key")
            parser.add_argument("name")
            parser.add_argument("category")
            parser.add_argument("videos", action='append')
            params = parser.parse_args()

            # Parameters must not be null
            if params["name"] is None or params["category"] is None or params["videos"] is None:
                raise

            # Check if user is authorized to PUT/POST/DELETE
            if params["key"] != protected.AUTHKEY:
                return "unauthorized"

            return TrickModel(
                uuid=str(uuid.uuid1()),  # Generate UUID for trick
                name=params["name"],
                discipline=str(discipline),
                category=params["category"],
                videos=params["videos"]
            )

        except Exception as e:
            print(e)
            return None
