from selenium import webdriver

browser = webdriver.Firefox()
browser.get('https://www.yahoo.com')

search_elem = browser.find_element_by_name('p')
search_elem.send_keys('Bill Cosby')

submit_elem = browser.find_element_by_id('search-submit')
submit_elem.submit()