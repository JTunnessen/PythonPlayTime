#! python3
# search5.py - How often do you just open one search result? This script opens the first 5 Google search results

import requests, sys, webbrowser, bs4
import time

from bs4 import BeautifulSoup

firefox = webbrowser.get('firefox')

print('Searching...') # display text while downloading the Google page
res = requests.get('http://google.com/search?q=' + ''.join(sys.argv[1:]))
res.raise_for_status()

# Retrieve top search results
soup = BeautifulSoup(res.text)

# Open a browser tab for each result
linkElems = soup.select('.r a')
numOpen = min(5, len(linkElems))
for i in range(numOpen):
	firefox.open('http://google.com' + linkElems[i].get('href'), new=2, autoraise=True)
	print('Opening a link..')
	time.sleep(.5)
