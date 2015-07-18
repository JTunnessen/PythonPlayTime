#! python3
# amazoned.py - This script blows up someone's browser by contnuously (10) opening Amazon searches

import requests, sys, webbrowser, bs4
import time

from bs4 import BeautifulSoup

firefox = webbrowser.get('firefox')

print('Pulling up Amazon...') # display text while downloading the Google page
res = requests.get('http://www.amazon.com/s/ref=nb_sb_noss_1?url=search-alias%3Daps&field-keywords=' + ''.join(sys.argv[1:]))
res.raise_for_status()

# Retrieve top search results
soup = BeautifulSoup(res.text)

# Open a browser tab for each result
linkElems = soup.select('.a-row a')
numOpen = min(10, len(linkElems))
for i in range(numOpen):
	firefox.open('http://amazon.com' + linkElems[i].get('href'), new=2, autoraise=True)
	print('Opening a link..')
	time.sleep(.5)
