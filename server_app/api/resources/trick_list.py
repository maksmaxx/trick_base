from flask_restful import Resource, reqparse
from services.mongo_client import MongoClient


class TrickList(Resource):
    """
    TrickList provides endpoints:
    GET     /api/tricks : Get all tricks
    POST    /api/tricks : Get all tricks belonging to discipline identified by "name"
        request:
        {
            "name": "<name>"
        }
    """

    def get(self):
        """
        GET     /api/tricks : Get all tricks
        """

        client = MongoClient()
        if client.connect():
            result = client.find_all_tricks()
            return result.to_json(), 200
        else:
            return "Service temporary unavailable", 503

    def post(self):
        """
        POST    /api/tricks : Get all tricks belonging to discipline identified by "name"
            request:
            {
                "discipline": "<name>"
            }
        """

        name = self.__process_arguments()
        if name is None:
            return "Invalid JSON data", 400

        client = MongoClient()
        if client.connect():
            if client.find_discipline_with_name(name) is not None:
                result = client.find_all_tricks_belonging_to(name)
                return result.to_json(), 200
            else:
                return "Discipline not found", 404
        else:
            return "Service temporary unavailable", 503

    def __process_arguments(self):
        """
        Gets name from incoming JSON
        :return: str or none
        """
        try:
            parser = reqparse.RequestParser()
            parser.add_argument("discipline")
            params = parser.parse_args()
            return params["discipline"]
        except Exception as e:
            print(e)
            return None
