# apicovid2019
It is the api created for covid-19 using flask, flask-Restful and scraped the online data
provided by [Worldometers](https://www.worldometers.info/coronavirus/).
The data is updated very early and fast in this site and getting the exact info is at right time
without any delay. This is hosted on heroku under [apicovid2019](https://apicovid2019.herokuapp.com).

For now I have only included our country's info, in comming commits I will be 
including overall important info.

This is a support project to the scheduled covid alert script emailing 
to the emails listed, running on its own at particular time of the day
with support of sendgrid.

Anyone searching for early info about covid data can use the site.
 
For now you can test using:

GET apicovid2019.herokuapp.com

or

curl apicovid2019.herokuapp.com

This gives you a json of result containing total world cases, cases by country name and by continent.

To fetch the specific result according to country name
use this:
Example:

GET apicovid2019.herokuapp.com/country=Nepal

or 

curl  apicovid2019.herokuapp.com/country=Nepal
