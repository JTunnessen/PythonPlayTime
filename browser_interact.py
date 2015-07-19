from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://chiefdigitalme.com')
try:
	elem = browser.find_element_by_link_text('The 10th Doctor')
	print('Found <%s> element with that class name!' % (elem.tag_name))
	elem.click() # Opens that element
except:
	print('Was not able to find an element with that name.')