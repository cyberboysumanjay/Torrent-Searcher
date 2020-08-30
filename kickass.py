from bs4 import BeautifulSoup as bs
import pyperclip
import requests

def kickass_search(query, doDownload):
    base_url="https://kickass.unblockit.top/search.php?q="
    url=base_url+query+'/'
    print("Searching......")
    source=requests.get(url).text
    soup=bs(source,'lxml')
    name=soup.find_all('a', class_="cellMainLink")
    results=[]
    i=1
    for r in name:
        print(i,r.text)
        i=i+1

    if doDownload == True:
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
