from flask import Flask
from flask_restful import Resource, Api
import api_co
app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return api_co.msg

api.add_resource(HelloWorld, '/')

#if __name__ == '__main__':
#    app.run(debug=True)
