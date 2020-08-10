from flask import Flask
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
GET 	/api/disciplines/{name} : Get the discipline identified by "name"
GET     /api/tricks : Get all tricks
POST    /api/tricks : Get all tricks belonging to discipline identified by "name"
GET     /api/tricks/{uuid} : Get the trick identified by "uuid"
"""

api.add_resource(DisciplineList, "/api/disciplines")
api.add_resource(Discipline, "/api/disciplines/<string:name>")
api.add_resource(TrickList, "/api/tricks")
api.add_resource(Trick, "/api/tricks/<string:uuid>")


"""
App routes - rendering HTML to be implemented later?
"""
@app.route("/")
def main():
    return "Hello, it's the Trick Base.", 200


if __name__ == '__main__':
    # TODO: CHECK DEBUG FLAG
    app.run(debug=True)
