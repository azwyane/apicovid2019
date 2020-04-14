# apicovid2019 
It is the api created for covid-19 using flask, flask-Restful and scraped the online data
provided by [Worldometers](https://www.worldometers.info/coronavirus/).
The data is updated very early and fast in this site and getting the exact info is at right time
without any delay. This is hosted on heroku under [apicovid2019](https://apicovid2019.herokuapp.com).


This is a support project to the scheduled covid alert script emailing 
to the emails listed, running on its own at particular time of the day
with support of sendgrid.

Anyone searching for early info about covid data can use the site.

##Fetch entire data 
To get the entire data, you can test using:
```
GET apicovid2019.herokuapp.com
```
or
```
curl apicovid2019.herokuapp.com
```
This gives you a json of result containing total world cases, cases by country name and by continent.

##Fetch data by specific country 
To fetch the specific result according to country name
use this:
Example:
```
GET apicovid2019.herokuapp.com/country=Nepal
```
or 
```
curl  apicovid2019.herokuapp.com/country=Nepal
```

##Fetch data by specific continent 
To fetch the specific result according to continent name.
###Available as:
   - Africa
   - Asia
   - Europe
   - Oceania
   - North America
   - South America

**Use this:**
Example:
```
GET apicovid2019.herokuapp.com/continent=Asia
```
or 
```
curl  apicovid2019.herokuapp.com/continent=Asia
```




