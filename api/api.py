from flask import Flask
from flask_restful import Api

from resources.discipline import Discipline
from resources.discipline_list import DisciplineList
from resources.trick import Trick
from resources.trick_list import TrickList

app = Flask(__name__)
api = Api(app)

""""
GET 	/device-management/devices : Get all devices
POST 	/device-management/devices : Create a new device

GET 	/device-management/devices/{id} : Get the device information identified by "id"
PUT 	/device-management/devices/{id} : Update the device information identified by "id"
DELETE	/device-management/devices/{id} : Delete device by "id"
"""

# Routes
api.add_resource(DisciplineList, "/api/disciplines")                # Returns all disciplines
api.add_resource(Discipline, "/api/discipline/<string:name>")       # Returns discipline
api.add_resource(TrickList, "/api/tricks/<string:discipline>")      # Returns all tricks of 1 discipline
api.add_resource(Trick, "/api/trick/<int:id>")                      # Returns trick

if __name__ == '__main__':
    # TODO - DELETE DEBUG
    app.run(debug=True)
