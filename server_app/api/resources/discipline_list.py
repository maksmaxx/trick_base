from flask_restful import Resource
from services.mongo_client import MongoClient


class DisciplineList(Resource):
    """
    DisciplineList provides endpoints:
    GET 	/api/disciplines : Get all disciplines
    """

    def get(self):
        """
        GET /api/disciplines : Get all disciplines
        """

        client = MongoClient()
        if client.connect():
            result = client.find_all_disciplines()
            return result.to_json(), 200
        else:
            return "Service temporary unavailable", 503
