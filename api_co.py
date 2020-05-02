import os
from bs4 import BeautifulSoup
import requests

try:
    '''
    previous version used to save a file
    called file.txt so minimize the request to
    the worldometers site and cache with the info
    to work within 30 min of heroku sleeping 
    due to inactivity
    os.system('rm file.txt')
    os.system('curl https://www.worldometers.info/coronavirus/ > file.txt')
    '''
   
    def data():
        
        res=requests.get("https://www.worldometers.info/coronavirus")
        h_source=res.text

    #except:
    #    print("error")
        
    #with open ('./file.txt') as h_source:   #this was used before to cache with response
                                            #as file.txt
        soup = BeautifulSoup(h_source, 'html.parser')
    
        title=["Country/other",
            "TotalCases",
            "NewCases",
            "TotalDeaths",
            "NewDeaths",
            "TotalRecovered",
            "ActiveCases",
            "Serious",
            "Totalcases/1Mpop",
            "Deaths/1Mpop",
            "TotalTests",
            "Tests/1Mpop"
            ]
        
        #conti=[]
        #value=[]
        #table = soup.find('table', {'class': 'table'})
        
        
        
        def globalwise():
            '''
            a=soup.select("#maincounter-wrap")#returns list of under that id
            names=[]
            for name in a:
                names.append((name.find("h1").string)[:-1].replace(" ",""))
        
            names_value=[]
            for name_val in a:
                names_value.append((name_val.find("span").string).strip())
        
            msg0=dict(list((n,v) for n,v in zip(names,names_value)))
            '''
            t=[
            "CoronavirusCases",
            "NewCases",
            "TotalDeaths",
            "NewDeaths",
            "TotalRecovered",
            "ActiveCases",
            "Serious",
            "Totalcases/1Mpop",
            "Deaths/1Mpop",
            ]
          
            names_value=[]
            a=soup.find_all(attrs={"class":"total_row","class":"total_row_body"})
          
            fval=a[0].find("td").findNext("td")
            for i in range(0,9):
                names_value.append(str(fval.string.strip()))
                fval=fval.findNext("td")
            msg0=dict(list((n,v) for n,v in zip(t,names_value)))

            return msg0
            
        
    ######
        
        def countrywise():
            val=[]
            msg1=[]  #list of country wise data
            a=soup.find_all(attrs={"class":"mt_a"})
            for index,country in enumerate(a):
                if index <=int(len(a)/2-1):                  #changed hardcoded index limit to be dynamic1
                    val.append(country.string)
                    for i in range(0,11):
                        country=country.findNext("td")
                        val.append(str(country.string).strip())
                    pre_msg=dict([(x,y) for x,y in zip(title,val)])
                    msg1.append(pre_msg)
                    del val[:]
                else:
                    del val[:]
                    break
            return msg1



    #####

        #continent wise
        def continentwise():
            
            a=soup.find_all(attrs={'class':"total_row_world row_continent"})
        
            names=[]     #list of continent names
            for index,name in enumerate(a):
                if index<=5:
                    names.append(name.find("nobr").string)
                else:
                    break
        
            next_val=[]
            msg2=[]   #list of continent wise data
            for continent in names:
                next_val.append(continent)
                b=soup.find("tbody").find("nobr",text=continent)
                for i in range (0,11):
                    b=b.findNext("td")
                    next_val.append(str(b.string).strip())
                    pre_msg=dict([(x,y) for x,y in zip(title,next_val)]) 
                msg2.append(pre_msg)
                del next_val[:]
            return msg2

    #####
        #final message    
        msg=[globalwise(),countrywise(),continentwise()]
        return msg
    
except Exception as e:
    msg=e
    

