import time

from selenium import webdriver

# Open a browser window in Firefox to the GMAIL sign in page
browser = webdriver.Firefox()
browser.get('http://gmail.com')

# Enter your email address into the Email form field
email_elem = browser.find_element_by_id('Email')
email_elem.send_keys('put_your_email@gmail.com')

# Click the NEXT button
next_elem = browser.find_element_by_id('next')
next_elem.click()

time.sleep(.5)

# Enter your password
password_elem = browser.find_element_by_id('Passwd')
password_elem.send_keys('add_your_password')

# Click the SUBMIT button
signIn_elem = browser.find_element_by_id('signIn')
signIn_elem.click()
