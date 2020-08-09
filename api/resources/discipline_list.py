from flask_restful import Resource, reqparse

from services.mongo_client import MongoClient
from models.discipline_list_model import DisciplineListModel
from models.discipline_model import DisciplineModel
import protected.const as protected


class DisciplineList(Resource):
    """
    DisciplineList provides endpoints:
    GET 	/api/disciplines : Get all disciplines
    POST 	/api/disciplines : Create a new discipline
    """

    def get(self):
        """
        GET 	/api/disciplines : Get all disciplines

        GET Json structure:
        {
            "disciplines": [
                {
                    "name": "skiing",
                    "area": "land",
                    "image": "img1"
                },
                { NEXT DISCIPLINE } ...
            ]
        }
        """

        client = MongoClient()
        if client.connect():
            result: DisciplineListModel = client.find_all_disciplines()
            return result.to_json(), 200

        # Connection to DB error
        else:
            return "Service temporary unavailable", 503

    def post(self):
        """
        POST    /api/disciplines : Create a new discipline
        Name needs to be unique! Check existed names with GET

        POST Json structure:
        {
            "key": "<authorization_key>",
            "name": "<name>",
            "area": "<area>",
            "image": "<image_path>"
        }
        """

        incoming = self.__process_arguments()
        if isinstance(incoming, DisciplineModel):
            client = MongoClient()
            if client.connect():
                # Create new discipline
                result = client.create_discipline(incoming)
                if result is not None:
                    return result.to_json(), 201
                else:
                    return "Already exists", 400

            elif incoming == "unauthorized":
                return "Unauthorized.", 401
            # Connection to DB error
            else:
                return "Service temporary unavailable", 503

        elif incoming == "unauthorized":
            return "Unauthorized", 401
        else:
            return "Invalid discipline parameters", 400

    def __process_arguments(self):
        """
        Validate parameters provided with JSON
        Returns None if error, DisciplineModel if success
        """

        try:
            parser = reqparse.RequestParser()
            parser.add_argument("key")
            parser.add_argument("name")
            parser.add_argument("area")
            parser.add_argument("image")
            params = parser.parse_args()

            # Parameters must not be null
            if params["image"] is None or params["area"] is None or params["name"] is None:
                raise

            # Check if user is authorized to PUT/POST/DELETE
            if params["key"] != protected.AUTHKEY:
                return "unauthorized"

            return DisciplineModel(
                image=params["image"],
                area=params["area"],
                name=params["name"],
            )

        except Exception as e:
            print(e)
            return None
