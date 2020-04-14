import os
from bs4 import BeautifulSoup


try:
    os.system('rm file.txt')
    os.system('curl https://www.worldometers.info/coronavirus/ > file.txt')
    

except:
    print("error")
    
with open ('./file.txt') as h_source:
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
    
    
    
        
    a=soup.select("#maincounter-wrap")#returns list of under that id
    names=[]
    for name in a:
        names.append(name.find("h1").string)
    
    names_value=[]
    for name_val in a:
        names_value.append(name_val.find("span").string)
    
    msg0=dict(list((n,v) for n,v in zip(names,names_value)))
    
######
      
      
    val=[]
    msg1=[]  #list of country wise data
    a=soup.find_all(attrs={"class":"mt_a"})
    for index,country in enumerate(a):
        if index <=209:
            val.append(country.string)
            for i in range(0,11):
                country=country.findNext("td")
                val.append(country.string)
            pre_msg=dict([(x,y) for x,y in zip(title,val)])
            msg1.append(pre_msg)
            del val[:]
        else:
            del val[:]
            break



#####

    #continent wise
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
            next_val.append(b.string)
            pre_msg=dict([(x,y) for x,y in zip(title,next_val)]) 
        msg2.append(pre_msg)
        del next_val[:]

#####
    #final message    
    msg=[msg0,msg1,msg2]
    

