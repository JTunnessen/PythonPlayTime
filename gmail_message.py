import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Open a browser window in Firefox to the GMAIL sign in page
browser = webdriver.Firefox()
browser.get('http://mail.google.com')

# Enter your email address into the Email form field
email_elem = browser.find_element_by_id('Email')
email_elem.send_keys('email_address@gmail.com')
print('Added the Email Address')

# Click the NEXT button
next_elem = browser.find_element_by_id('next')
next_elem.click()
print('Clicked Next')

time.sleep(.5)

# Enter your password
password_elem = browser.find_element_by_id('Passwd')
password_elem.send_keys('my_password')
print('Added the Password')

# Click the SUBMIT button
signIn_elem = browser.find_element_by_id('signIn')
signIn_elem.click()
print('Signed in to GMAIL')
print('Waiting for Element to Load')

try:
	element = WebDriverWait(browser, 15).until(
		EC.presence_of_element_located((By.CLASS_NAME, "T-I J-J5-Ji T-I-KE L3")))
finally:
	browser.quit()


# Adding sending an email
compose_elem = browser.find_element_by_class_name("T-I J-J5-Ji T-I-KE L3")
compose_elem.submit()
print('Clicked Compose Email')

#time.sleep(1)

#to_elem = browser.find_element_by_class_name('v0')
#to_elem.send_keys('other_email_address@yahoo.com')
#print('Added the TO: Address')

#subject_elem = browser.find_element_by_class_name('aoT')
#subject_elem.send_keys('Automated Trial Run')
#print('Added the Subject')

#body_elem = browser.find_element_by_id(':zr')
#body_elem.send_keys('This is what I am going to say.')
#print('Added the Body')

#send_elem = browser.find_element_by_id(':yf')
#send_elem.submit()
#print('Sent the email')