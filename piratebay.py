from bs4 import BeautifulSoup as bs
import pyperclip
import requests

def piratebay_search(query):
    scrapper_api='https://api.scraperapi.com/?key=2500866341976677504461594942127656&url='
    url=scrapper_api+'https://pirateproxy.mx/search/'+query+'/0/99/0'
    print("Searching......")
    source=requests.get(url).text
    soup=bs(source,'lxml')
    results=soup.find_all('div',class_='detName')
    i=1
    for r in results:
        print(i,r.text)
        i=i+1
    print("Enter the Serial Number of the search item you like to download: ")
    choice=int(input())
    print ("Fetching data.....")
    magnet_results=soup.find_all('a',title='Download this torrent using magnet')
    a=[]
    for m in magnet_results:
        a.append(m['href'])
    magnet_link=(a[choice-1])
    print("Magnet Link of your selected choice has been fetched.")
    pyperclip.copy(magnet_link)
    print ("Your magnet link is now in your clipboard.")
