from flask import Flask, render_template
from flask_restful import Api

from api.resources.discipline import Discipline
from api.resources.discipline_list import DisciplineList
from api.resources.trick import Trick
from api.resources.trick_list import TrickList

app = Flask(__name__)
api = Api(app)

"""
Api routes

GET 	/api/disciplines : Get all disciplines
POST 	/api/disciplines : Create a new discipline

GET 	/api/discipline/{name} : Get the discipline information identified by "name"
PUT 	/api/discipline/{name} : Update the discipline information identified by "name"
DELETE	/api/discipline/{name} : Delete the discipline identified by "name"(and all associated tricks)

GET     /api/tricks/{discipline_name} : Get all tricks belonging to discipline identified by "discipline_name"
POST    /api/tricks/{discipline_name} : Create a new trick belonging to discipline identified by "discipline_name"

GET     /api/trick/{uuid} : Get the trick identified by "uuid"
PUT     /api/trick/{uuid} : Update the trick identified by "uuid"
DELETE  /api/trick/{uuid} : Delete the trick identified by "uuid"
"""

api.add_resource(DisciplineList, "/api/disciplines")
api.add_resource(Discipline, "/api/discipline/<string:name>")
api.add_resource(TrickList, "/api/tricks/<string:discipline>")
api.add_resource(Trick, "/api/trick/<string:uuid>")


@app.route("/")
def main():
    return "Hello Trick Base", 200


if __name__ == '__main__':
    # TODO - DELETE DEBUG
    app.run(debug=False)
