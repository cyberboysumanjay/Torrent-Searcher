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

def kickass_search(query):
    scrapper_api='https://api.scraperapi.com/?key=2500866341976677504461594942127656&url='
    base_url="https://kickass.unblocked.vet/usearch/"
    url=scrapper_api+base_url+query+'/'
    print("Searching......")
    source=requests.get(url).text
    soup=bs(source,'lxml')
    name=soup.find_all('a', class_="cellMainLink")
    results=[]
    i=1
    for r in name:
        print(i,r.text)
        i=i+1
    print("Enter the Serial Number of the search item you like to download: ")
    choice=int(input())
    print ("Fetching data.....")
    magnet=soup.find_all('a', title="Torrent magnet link")
    a=[]
    for m in magnet:
        a.append(m['href'])
    magnet_link=(a[choice-1])
    print("Magnet Link of your selected choice has been fetched.")
    pyperclip.copy(magnet_link)
    print ("Your magnet link is now in your clipboard.")

n=int(input("Enter your preferred Torrent Search Engine:\n 1: ThePirateBay\n 2: Kickass\n"))
query=input("Enter your query\n")
if n==1:
    piratebay_search(query)
elif n==2:
    kickass_search(query)
else:
    print("Please try again!")
