from flask_restful import Resource
from services.mongo_client import MongoClient


class Discipline(Resource):
    """
    Discipline provides endpoints:
    GET 	/api/disciplines/{name} : Get the discipline identified by "name"
    """

    def get(self, name):
        """
        GET /api/discipline/{name} : Get the discipline identified by "name"
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
