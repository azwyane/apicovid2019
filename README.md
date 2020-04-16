# apicovid2019 
It is the api created for covid-19 using flask, flask-Restful and scraped the online data
provided by [Worldometers](https://www.worldometers.info/coronavirus/).
The data is updated very early and fast in this site and getting the exact info is at right time
without any delay. 

## Hosting
This project is hosted on two servers maintained separately but having same response.
You can call the api on any of these two sites:

- heroku under [apicovid2019](https://apicovid2019.herokuapp.com).
- azure under [apicovid2019](https://apicovid2019.azurewebsites.net).

This is a support project to the scheduled covid alert script emailing 
to the emails listed, running on its own at particular time of the day
with support of sendgrid.

Anyone searching for early info about covid data can use the site.

## Fetch entire data 
To get the entire data, you can test:

- **using GET**
```
GET apicovid2019.herokuapp.com
```
or
 
```
GET apicovid2019.azurewebsites.net
```

- **using curl**
```
curl apicovid2019.herokuapp.com
```
or

```
curl apicovid2019.azurewebsites.net
```
This gives you a json of result containing total world cases, cases by country name and by continent.

## Fetch data by specific country 
To fetch the specific result according to country name
use this:
Example:

- **using GET**
```
GET apicovid2019.herokuapp.com/country=Nepal
```
or 

```
GET apicovid2019.azurewebsites.net/country=Nepal
```

- **using curl**
```
curl  apicovid2019.herokuapp.com/country=Nepal
```

```
curl apicovid2019.azurewebsites.net/country=Nepal
```

## Fetch data by specific continent 
To fetch the specific result according to continent name.
### Available as:
   - Africa
   - Asia
   - Europe
   - Oceania
   - North America
   - South America

**Use this:**
Example:

- **using GET**
```
GET apicovid2019.herokuapp.com/continent=Asia
```
or

```
GET apicovid2019.azurewebsites.net/continent=Asia
```


- **using curl** 
```
curl  apicovid2019.herokuapp.com/continent=Asia
```
or

```
curl apicovid2019.azurewebsites.net/continent=Asia
```



