#! python3
# social_me.py opens all my usual social networks with one script
import webbrowser
import time

firefox = webbrowser.get('firefox')
url_list = ['https://twitter.com/JimT2', 'https://linkedin.com/in/jimtunnessen', 'https://plus.google.com/+JimTunnessen/posts']

for url in url_list:
	firefox.open(url, new=2, autoraise=True)
	print('Opening url')
	time.sleep(.5)