from bs4 import BeautifulSoup as bs
import pyperclip
import requests
import zooqle
import kickass
import piratebay
import spell

query=input("Enter your query\n")
query=str(spell.Check(query))
print("Searching for :",query)

n=int(input("Enter your preferred Torrent Search Engine:\n 1: ThePirateBay\n 2: Kickass\n 3: Zooqle\n 4: All\n"))

if n==1:
    piratebay.piratebay_search(query, True)
elif n==2:
    kickass.kickass_search(query, True)
elif n==3:
    zooqle.zooqle_search(query, True)
elif n == 4:
    print("Searching ThePirateBay")
    print("-----------------------")
    piratebay.piratebay_search(query, False)

    print("Searching Kickass")
    print("-----------------------")
    kickass.kickass_search(query, False)
    
    print("Searching Zooqle")
    print("-----------------------")
    zooqle.zooqle_search(query, False)
else:
    print("Please try again!")
