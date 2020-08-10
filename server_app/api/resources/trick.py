from flask_restful import Resource, reqparse
from services.mongo_client import MongoClient


class Trick(Resource):
    """
    Trick provides endpoints:
    GET     /api/tricks/{uuid} : Get the trick identified by "uuid"
    """

    def get(self, uuid):
        """
        GET /api/tricks/{uuid} : Get the trick identified by "uuid"
        """

        client = MongoClient()
        if client.connect():
            trick = client.find_trick_with_uuid(uuid)
            if trick is not None:
                return trick.to_json(), 200
            else:
                return "Trick not found", 404
        else:
            return "Service temporary unavailable", 503
