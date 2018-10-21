import json
from bs4 import BeautifulSoup as bs
import requests
import urllib.parse
import pyperclip
import colored
from colored import stylize
import re

def zooqle_search(query):
    url='https://zooqle.unblocked.gdn/search?q='+query
    print("Searching......")
    source=requests.get(url).text
    soup=bs(source,'lxml')
    magnet_results=soup.find_all('a',title='Magnet link',href=True)
#    print(magnet_results)
    i=1
    for a in soup.find_all('a',class_=' small', href=True):
        print (i," :", a['href'][1:-11])
        print()
        i+=1

    index=int(input("Select one from the list below: \n"))
    m=[]
    for links in magnet_results:
        m.append(links['href'])
    magnet_link=m[index-1]
#    print(magnet_link)
    pyperclip.copy(magnet_link)
    print("Magnet link of the selected movie is copied to clipboard!")



#zooqle_search(query)
