from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import csv
import pandas as pd

def veri_cek():
    
    sayfa = int(input("scroll sayısını girin = "))

    driver_path = "notes/chromedriver.exe"
    browser = webdriver.Chrome(driver_path)

    browser.get("https://www.google.com.tr/")
    yazı_girişi = browser.find_element_by_css_selector(".gLFyf.gsfi")
    yazı_girişi.send_keys("twitter deep learning türkiye")
    time.sleep(2)
    yazı_girişi.send_keys(Keys.ENTER)

    tıkla = browser.find_element_by_css_selector(".zTpPx.V7Sr0.p5AXld")
    tıkla.click()
    
    #
    file = open("tweetler.csv","w",encoding="utf-8")
    writer = csv.writer(file)
    writer.writerow(["tweetler","begeni_sayisi","yorum_sayisi","retweet_sayisi"])
    
    
    #
    a = 0
    while a < sayfa:
    #
        lastHeight = browser.execute_script("return document.body.scrollHeight")
        i=0
        while i<1:
            browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)
            newHeight = browser.execute_script("return document.body.scrollHeight")

            if newHeight == lastHeight:
                break
            else:
                lastHeight = newHeight

            i = i+1

        sayfa_kaynağı = browser.page_source
        soup = BeautifulSoup(sayfa_kaynağı, "html.parser")
        tweetler = soup.find_all("div",attrs={"data-testid":"tweet"})


        for i in tweetler:
            
            try:
                
                yazı = i.find("div", attrs={"class":"css-901oao r-hkyrab r-1qd0xha r-a023e6 r-16dba41 r-ad9z0x r-bcqeeo r-bnwqim r-qvutc0"}).text
                yorum_sayısı = i.find("div", attrs={"data-testid":"reply"}).text
                retweet_sayısı = i.find("div", attrs={"data-testid":"retweet"}).text
                beğeni_sayısı = i.find("div", attrs={"data-testid":"like"}).text

                writer.writerow([yazı,beğeni_sayısı,yorum_sayısı,retweet_sayısı])
            
            except:
                print("**")
        a = a+1


veri_cek()