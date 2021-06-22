from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import urllib

# Access to Twitter
url = r'https://twitter.com/MERAL____/status/1321962410366935040'
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(url)

#driver.save_screenshot("screenshot.png")

#with open('filename.png', 'wb') as file:
#    file.write(driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/section/div/div/div[2]/div/div/article/div/div/div/div[2]/div[1]/div/div/a/div[2]').screenshot_as_png)
    

# get the image source
img = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/section/div/div/div[2]/div/div/article/div/div/div/div[2]/div[1]/div/div/a/div[2]')
src = img.get_attribute('src')

# download the image
urllib.urlretrieve(src, "captcha.png")

driver.close()