from flask import Flask
from flask_restful import Api
from resources.discipline import Discipline

app = Flask(__name__)
api = Api(app)

# Routes
api.add_resource(Discipline, "/disciplines/<string:name>")

if __name__ == '__main__':
    # TODO - DELETE DEBUG
    app.run(debug=True)
