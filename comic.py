# Loads the XKCD Comic home page
# Saves the comic image on that page
# Follows the previous comic link
# Repeats until it reaches the first 

#! python3
# comic.py - Downloads every single XKCD comic

import requests, os, bs4

from bs4 import BeautifulSoup


url = 'http://xkcd.com' #starting url
if not os.path.exists('xkcd'):
	os.makedirs('xkcd') # Store comics in ./xkcd

while not url.endswith('#'):
	# Download the page
	print('Downloading page...')
	res = requests.get(url)
	res.raise_for_status()

	soup = BeautifulSoup(res.text)

	# Find the URL of the comic image
	comic_elem = soup.select('#comic img')
	if comic_elem == []:
		print('Could not find comic image')
	else:
		comic_url = 'http:' + comic_elem[0].get('src')
		# Download the image
		print('Downloading image...')
		res = requests.get(comic_url)
		res.raise_for_status()
	
	# Save the image to ./xkcd
	image_file = open(os.path.join('xkcd', os.path.basename(comic_url)), 'wb')
	for chunk in res.iter_content(100000):
		image_file.write(chunk)
	image_file.close()

	# Get the Prev button's url
	prev_link = soup.select('a[rel="prev"]')[0]
	url = 'http://xkcd.com' + prev_link.get('href')


print('Done')

