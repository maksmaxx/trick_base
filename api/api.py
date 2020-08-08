from flask import Flask
from flask_restful import Api

from resources.discipline import Discipline
from resources.discipline_list import DisciplineList
from resources.trick import Trick
from resources.trick_list import TrickList

app = Flask(__name__)
api = Api(app)

""""
Api routes

GET 	/api/disciplines : Get all disciplines
POST 	/api/disciplines : Create a new discipline

GET 	/api/discipline/{name} : Get the discipline information identified by "name"
PUT 	/api/discipline/{name} : Update or create the discipline information identified by "name"
DELETE	/api/discipline/{name} : Delete the discipline identified by "name"

GET     /api/tricks/{discipline_name} : Get all tricks belonging to discipline identified by "discipline_name"
POST    /api/tricks : Create a new trick

GET     /api/trick/{id} : Get the trick identified by "id"
PUT     /api/trick/{id} : Update or create the trick identified by "id"

"""

api.add_resource(DisciplineList, "/api/disciplines")
api.add_resource(Discipline, "/api/discipline/<string:name>")
api.add_resource(TrickList, "/api/tricks", "/api/tricks/<string:discipline>")
api.add_resource(Trick, "/api/trick/<int:id>")

if __name__ == '__main__':
    # TODO - DELETE DEBUG
    app.run(debug=True)
