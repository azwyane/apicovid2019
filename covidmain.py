from flask import Flask
from flask_restful import Resource, Api
from api_co import dataProcessor


app = Flask(__name__)
api = Api(app)

class Global_data(Resource):
    '''
    It is the class of first endpoint '/'
    It has a get funtion that return a list of json
    of corona virus status scraped from
    https://www.worldometers.info/coronavirus/
    
    The first item in list is a dictionary of world
    covid-19 status.
    The second item in list is a list of dictionary
    of covid-19 status in each country's of the world.
    The third item in the list are dictionary's of
    covid-19 status by continent.
    '''
   
    def get(self):
    
       self.datum=dataProcessor().globalwise()
       return self.datum

class Country_data(Resource):
    '''
    It is the class of second endpoint '/country=<string:country>'
    It has a get funtion that return a json
    of corona virus status scraped from
    https://www.worldometers.info/coronavirus/
    
    country is the parameter passed to the endpoint.
    Example
    GET apicovid2019.herokuapp.com/country=Nepal
    
    The site apicovid2019.heroku.com is the site where
    it is hosted on. 
    It returns info of covid-19 status in the requested
    country of the world.
    ''' 

    def get(self,country):
        self.country=country
        self.datum=dataProcessor().countrywise()
        try:
            for i in self.datum:
                if i['Country/other']== self.country:
                    self.countr_y=i
                    break
            return self.countr_y
        except:
            return "Make sure to enter proper input and its method"

class Continent_data(Resource):
    '''
    It is the class of third endpoint '/continent=<string:continent>'
    It has a get funtion that return a json
    of corona virus status scraped from
    https://www.worldometers.info/coronavirus/
    
    country is the parameter passed to the endpoint.
    Example
    GET apicovid2019.herokuapp.com/continent=Asia
    
    The site apicovid2019.heroku.com is the site where
    it is hosted on. 
    It returns info of covid-19 status in the requested
    continent of the world.
    
    The available continents names are as:
    Africa
    Asia
    Europe
    Oceania
    North America
    South America
    ''' 
   
    def get(self,continent):
        self.continent=continent
        self.datum=dataProcessor().continentwise()
        try:
            for i in self.datum:
                if i['Country/other']== self.continent:
                    self.cont_y=i
                    break
            return self.cont_y
        except:
            return "Make sure to enter proper input and its method"

#endpoints of the api
api.add_resource(Global_data, '/')
api.add_resource(Country_data,'/country=<string:country>')
api.add_resource(Continent_data,'/continent=<string:continent>')

#if __name__ == '__main__':
#    app.run(debug=True)
