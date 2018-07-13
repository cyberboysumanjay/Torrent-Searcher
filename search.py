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

n=int(input("Enter your preferred Torrent Search Engine:\n 1: ThePirateBay\n 2: Kickass\n 3: Zooqle\n"))

if n==1:
    piratebay.piratebay_search(query)
elif n==2:
    kickass.kickass_search(query)
elif n==3:
    zooqle.zooqle_search(query)
else:
    print("Please try again!")
