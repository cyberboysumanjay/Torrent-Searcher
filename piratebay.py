from bs4 import BeautifulSoup as bs
import pyperclip
import requests


def piratebay_search(query, doDownload):
    url = 'https://pirateproxy.gdn/search/' + query + '/0/99/0'
    print("Searching......")
    source = requests.get(url).text
    soup = bs(source, 'lxml')
    results = soup.find_all('div', class_='detName')
    i = 1
    for r in results:
        print(i, r.text)
        i = i + 1

    if doDownload:
        print("Enter the Serial Number of the search item you like to download: ")
        choice = int(input())
        print("Fetching data.....")
        magnet_results = soup.find_all(
            'a', title='Download this torrent using magnet')
        a = []
        for m in magnet_results:
            a.append(m['href'])
        magnet_link = (a[choice - 1])
        print("Magnet Link of your selected choice has been fetched.")
        pyperclip.copy(magnet_link)
        print("Your magnet link is now in your clipboard.")
