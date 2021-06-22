from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time

# Step 1) Open Chrome 
driver = webdriver.Chrome(r'C:\Users\HknMz\Desktop\github\selenium\chromedriver_win32\chromedriver.exe')
driver.get("http://www.facebook.com")

# Step 3) Search & Enter the Email or Phone field & Enter Password
username = driver.find_element_by_id("email")
password = driver.find_element_by_id("pass")
submit   = driver.find_element_by_id("loginbutton")
username.send_keys("YOUR EMAILID")
password.send_keys("YOUR PASSWORD")
WebDriverWait( driver, 500 )

# Step 4) Click Login
submit.click()
wait = WebDriverWait( driver, 5 )
page_title = driver.title
assert page_title == "Facebook"