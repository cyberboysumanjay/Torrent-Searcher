from bs4 import BeautifulSoup as bs
import pyperclip
import requests
# import json
# import urllib.parse
# import colored
# from colored import stylize
# import re


def zooqle_search(query, doDownload):
    url = "https://zooqle.unblockit.top/search?q=" + query
    print("Searching......\n")
    source = requests.get(url).text
    soup = bs(source, 'lxml')
    table_entries = soup.find_all('tr')
    magnet_links = []

    ind = 1

    for i in table_entries:
        if i.contents[1].text is not '':
            print(ind, i.contents[1].text)
            print()
            ind += 1
        try:
            magnet_links.append(i.contents[2].ul.contents[1].a['href'])
        except:
            pass

        

    if doDownload:
        index = int(input("Select one from the list below: \n"))
        print()
        
        magnet_link = magnet_links[index - 1]
        # print(magnet_link)
        pyperclip.copy(magnet_link)
        print("Magnet link of the selected movie is copied to clipboard!")


# zooqle_search(query, True)
