import os
from bs4 import BeautifulSoup

try:
    os.system('rm file.txt')
    os.system('curl https://www.worldometers.info/coronavirus/ > file.txt')
    

except:
    print("error")
    
with open ('./file.txt') as h_source:
    soup = BeautifulSoup(h_source, 'html.parser')
   # print(soup.prettify())
    value=[]
    table = soup.find('table', {'class': 'table'})
    th = table.find('td', text='Nepal')
    for i in range(0,10):
        value.append(th.string)
        th = th.findNext('td')

    msg={
        'Country':value[0],
        'Total cases':value[1],
        'New':value[2],
        'Total deaths':value[3],
        'New deaths':value[4],
        'Total recovered':value[5],
        'Active cases':value[6],
        'Serious cases':value[7],
        'Total cases per 1M':value[8],
        'Deaths per 1M':value[9]
        }
