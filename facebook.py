import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

#This part is for opening the webdriver with proxy (since FB is prohibited here!)
proxy="127.0.0.1:0000"
chrome_options=webdriver.ChromeOptions()
chrome_options.add_argument('--proxy-server=socks5://' + proxy)
driver=webdriver.Chrome('notes/chromedriver.exe',options=chrome_options)

# Let's open the FB and insert Username and Password:
driver.get("https://www.facebook.com")

# Give the username by copying the full XPath and send keys:
driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/div/div/div/div[2]/form/table/tbody/tr[2]/td[1]/input").send_keys("Username") 

#Same for the Password:
driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/div/div/div/div[2]/form/table/tbody/tr[2]/td[2]/input").send_keys("Password")

#Click the login button, you also can send Return key to password field:
driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/div/div/div/div[2]/form/table/tbody/tr[2]/td[3]/label/input").click()

#Hitting the status bar:
driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div[3]/div/div/div[1]/div[1]/div/div[2]/div/div/div[3]/div/div[2]/div/div/div/div[1]/div/div[1]/div").click() 

#giving the status message:
driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div[2]/div[2]/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div/div/div/div").send_keys("This is a test status from an automation :)")

#Hit the Post button:
driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div[2]/div[3]/div[2]/div").click()

#Enjoy the code :)