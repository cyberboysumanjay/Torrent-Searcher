from bs4 import BeautifulSoup as bs
import pyperclip
import requests
import json

MAGNET_TEMPLATE = "magnet:?xt=urn:btih:{0}&dn={1}&tr=udp%3A%2F%2Ftracker.coppersurfer.tk%3A6969%2Fannounce&tr=udp%3A%2F%2F9.rarbg.me%3A2850%2Fannounce&tr=udp%3A%2F%2F9.rarbg.to%3A2920%2Fannounce&tr=udp%3A%2F%2Ftracker.opentrackr.org%3A1337&tr=udp%3A%2F%2Ftracker.leechers-paradise.org%3A6969%2Fannounce"

def get_size_from_bytes(bytes):
    B = float(bytes)
    KB = float(1024)
    MB = float(KB ** 2) # 1,048,576
    GB = float(KB ** 3) # 1,073,741,824
    TB = float(KB ** 4) # 1,099,511,627,776

    if B < KB:
        return '{0} {1}'.format(B,'Bytes' if 0 == B > 1 else 'Byte')
    elif KB <= B < MB:
        return '{0:.2f} KB'.format(B/KB)
    elif MB <= B < GB:
        return '{0:.2f} MB'.format(B/MB)
    elif GB <= B < TB:
        return '{0:.2f} GB'.format(B/GB)
    elif TB <= B:
        return '{0:.2f} TB'.format(B/TB)

def piratebay_search(query, doDownload):
    url='https://apibay.org/q.php?q='+query
    print("Searching......")
    source = requests.get(url).text
    results = json.loads(source)
    if not(len(results)):
        print("No results found, Try another query...")
    
    for i,r in enumerate(results):
        print(i+1,r['name'],get_size_from_bytes(r['size']))

    if doDownload == True:
        print("Enter the Serial Number of the search item you like to download: ")
        choice=int(input())
        print ("Fetching data.....")
        magnet_link=MAGNET_TEMPLATE.format(results[choice-1]["info_hash"], results[choice-1]["name"])
        print("Magnet Link of your selected choice has been fetched.")
        pyperclip.copy(magnet_link)
        print ("Your magnet link is now in your clipboard.")
