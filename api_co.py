import os
from bs4 import BeautifulSoup

#try:
#    os.system('rm file.txt')
#    os.system('curl https://www.worldometers.info/coronavirus/ > file.txt')
    

#except:
#    print("error")
    
with open ('./file.txt') as h_source:
    soup = BeautifulSoup(h_source, 'html.parser')
   # print(soup.prettify())
    title=["Country/other",
           "TotalCases",
           "NewCases",
           "TotalDeaths",
           "NewDeaths",
           "TotalRecovered",
           "ActiveCases",
           "Serious",
           "Totalcases1Mpop",
           "Deaths",
           "TotalTests",
           "Tests",
           "1Mpop"]

    conti=[]
    value=[]
    table = soup.find('table', {'class': 'table'})
    
    
    
        
    a=soup.select("#maincounter-wrap")#returns list of under that id
    names=[]
    for name in a:
        names.append(name.find("h1").string)
    
    names_value=[]
    for name_val in a:
        names_value.append(name_val.find("span").string)
    
    msg0=dict(list((n,v) for n,v in zip(names,names_value)))
    
    ######
      
   # for child in table.tbody.tr.children:
   #     print(child)
    
   # a=soup.find('div')
   # for wick in range(0,10):
       # a= a.findNext('div')
       # print(a.string)
    
    
    
    #value=[]
    #th = table.find('td', text='Nepal')
    #for i in range(0,12):
    #    value.append(th.string)
    #    th = th.findNext('td')

    #msg1=dict([(x,y) for x,y in zip(title,value)])
    #msg1={
    #    'Country':value[0],
    #    'Total cases':value[1],
    #    'New':value[2],
    #    'Total deaths':value[3],
    #    'New deaths':value[4],
    #    'Total recovered':value[5],
    #    'Active cases':value[6],
    #    'Serious cases':value[7],
    #    'Total cases per 1M':value[8],
    #    'Deaths per 1M':value[9]
    #    }
    
    ###
    #country wise
    val=[]
    msg1=[]
    a=soup.find_all(attrs={"class":"mt_a"})
    for index,country in enumerate(a):
        if index <=219:
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





    #continent wise
    a=soup.find_all(attrs={'class':"total_row_world row_continent"})
   
    names=[]
    for index,name in enumerate(a):
        if index<=5:
            names.append(name.find("nobr").string)
        else:
            break
    #print(names)
    next_val=[]
    msg2=[]
    for continent in names:
        next_val.append(continent)
        b=soup.find("tbody").find("nobr",text=continent)
        for i in range (0,11):
            next_val.append(b.findNext("td").string)
        pre_msg=dict([(x,y) for x,y in zip(title,next_val)]) 
        msg2.append(pre_msg)
        del next_val[:]

    
    msg=[msg0,msg1,msg2]
    
