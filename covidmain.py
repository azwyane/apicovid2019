from flask import Flask
from flask_restful import Resource, Api
import api_co
import json
app = Flask(__name__)
api = Api(app)

class Home(Resource):
    def get(self):
        return json.dumps(api_co.msg,indent=2)

class Country_data(Resource):
    
    def get(self,country):
        self.country=country
        try:
            for i in api_co.msg[1]:
                if i['Country/other']== country:
                    self.countr_y=i
                    break
            return self.countr_y
        except:
            return "Make sure to enter proper input and its method"
api.add_resource(Home, '/')
api.add_resource(Country_data,'/country=<string:country>')
#if __name__ == '__main__':
#    app.run(debug=True)
