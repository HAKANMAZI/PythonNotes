import sys 

class PythonNotes():
    def __init__(self) -> None:
        pass
      
    def fibonacci(self, n): 
        '''write Fibonacci series up to n'''
        a, b = 0, 1
        while a < n:
            print(a, end=' ')
            a, b = b, a+b
  
    def fibonacci2(self, n): 
        '''return Fibonacci series up to n'''
        result = []
        a, b = 0, 1
        while a < n:
            result.append(a)
            a, b = b, a+b
        print(result) 

    def beautifulsoup(self):
        import requests
        from bs4 import BeautifulSoup

        contents = requests.get('https://twitter.com/i/status/1382727373494362118')
        soup = BeautifulSoup(contents.text, 'html.parser')

        file = open('soup.txt', "w")
        file.writelines(str(soup))
        print(soup)

    def readWriteFile(self):
        pass

    def beautifulsoupTweets(self):
        from bs4 import BeautifulSoup
        import requests

        page = requests.get("https://twitter.com/search?q=hakan&src=typed_query")
        soup = BeautifulSoup(page.content, "html.parser")
        tweetler = soup.find_all("div",attrs={"data-testid":"tweet"})


        for i in tweetler:
            yazi = i.find("div", attrs={"class":"css-901oao r-hkyrab r-1qd0xha r-a023e6 r-16dba41 r-ad9z0x r-bcqeeo r-bnwqim r-qvutc0"}).text
            yorum_sayisi = i.find("div", attrs={"data-testid":"reply"}).text
            retweet_sayisi = i.find("div", attrs={"data-testid":"retweet"}).text
            begeni_sayisi = i.find("div", attrs={"data-testid":"like"}).text
            print(yazi)
            print(yorum_sayisi)
            print(begeni_sayisi)

    def beautifulsoupNotes(self):
        from bs4 import BeautifulSoup
        import requests

        page = requests.get("https://twitter.com/search?q=hakan&src=typed_query")
        soup = BeautifulSoup(page.content, "html.parser")
        tweetler = soup.find_all("div",attrs={"class":"css-1dbjc4n"})
        #print(tweetler)

        for i in tweetler:

            print(i.find("div", attrs={"class":"css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0"}))
            '''    
            print(i.find("div", attrs={"data-testid":"reply"}))
            
            yazi = i.find("div", attrs={"class":"css-901oao r-hkyrab r-1qd0xha r-a023e6 r-16dba41 r-ad9z0x r-bcqeeo r-bnwqim r-qvutc0"}).text
            yorum_sayisi = i.find("div", attrs={"data-testid":"reply"}).text
            retweet_sayisi = i.find("div", attrs={"data-testid":"retweet"}).text
            begeni_sayisi = i.find("div", attrs={"data-testid":"like"}).text
            print(yazi)
            print(yorum_sayisi)
            print(begeni_sayisi)
            '''


        soup = BeautifulSoup("""<div class="systemRequirementsMainBox">
        <div class="systemRequirementsRamContent">
        <span title="000 Plus Minimum RAM Requirement">1 GB</span> </div>""", "xml")

        print(soup.select_one("span[title*=RAM]").text)
        # 1 GB

        import re
        print(soup.find("span", title=re.compile("RAM")).text)
        # 1 GB


        from bs4 import BeautifulSoup 
        r  = requests.get("http://www.game-debate.com/games/index.php?g_id=21580&game=000%20Plus").content

        soup = BeautifulSoup(r,"lxml")
        cont = soup.select_one("div.systemRequirementsRamContent")
        ram = cont.select_one("span")
        print(ram["title"], ram.text)
        for span in soup.select("div.systemRequirementsSmallerBox.sysReqGameSmallBox span"):
                print(span["title"],span.text)

    def os_Notes(self):
        import os 
        os.system("ls -l")
        os.system("python tweet.py")

    def gtts_Notes(self):
        from gtts import gTTS
        tts = gTTS('Hello Python')
        tts.save("hiPython.mp3") 

    def getpass_Notes(self):
        import getpass
        user = getpass.getuser()
        password = getpass.getpass()
        warning = getpass.GetPassWarning

    def tqdm_Notes(self):
        from tqdm import tqdm
        import time

        for a in tqdm(range(100)):
            time.sleep(2)

    def request_Notes(self):
        import requests
        x = requests.get('https://hakanmazi123.medium.com/')
        print(x.text)

    def pyscreenshot_Notes(self):
        import pyscreenshot
        image = pyscreenshot.grab()
        image.save("image.png")       

    def DirectoryTree_Notes(self):
        #pip install directory-tree-generator
        from DirectoryTree import TreeGenerator
        Tree = TreeGenerator()
        Tree.generate(r'C:\Users\HknMz\Desktop\github\instagram-medium')

    def ascii_magic_Notes(self):
        ''' pip install ascii_magic
        Fotoyu karakterler ile tekrardan çizer '''
        import ascii_magic
        output = ascii_magic.from_image_file('4.jpg')
        ascii_magic.to_terminal(output)

    def requests_html_Notes(self):
        '''amazon ürünlerini indirelim'''
        from requests_html import HTMLSession
        def getPrice(url):
            s = HTMLSession()
            r = s.get(url)
            r.html.render(sleep=1)

            product = {
                'title' : r.html.xpath('//*[@id="productTitle"]',first=True).text,
                'price' : r.html.xpath('//*[@id="priceblock_saleprice"]',first=True).text,
                'asin': r.html.xpath('//*[@id="productDetails_detailBullets_sections1"]/tbody/tr[4]/td',first=True).text
            }
            print(product['asin'])


        getPrice('https://www.amazon.com/DIGITNOW-Capture-Streaming-Camcorders-Action/dp/B08DQYNDWN/ref=sr_1_1_sspa?dchild=1&fst=as%3Aoff&pf_rd_i=16225007011&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=74069509-93ef-4a3c-8dca-a9e3fa773a64&pf_rd_r=MH4TJVCSJ5SHXFF9N0WY&pf_rd_s=merchandised-search-4&pf_rd_t=101&qid=1617913808&rnid=16225007011&s=computers-intl-ship&sr=1-1-spons&psc=1&smid=A1K8Z5DTHS1A1S&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzQTNEVkZaTU9OOVUmZW5jcnlwdGVkSWQ9QTAzNzMyNjAzNVZDTENUU1dJRUFSJmVuY3J5cHRlZEFkSWQ9QTA2NDgxMjExOUFESVVaNlJKSEFEJndpZGdldE5hbWU9c3BfYXRmX2Jyb3dzZSZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU=')

    def twitterScrape_Notes(self):
        import time
        from selenium import webdriver
        from selenium import common
        from selenium.webdriver.common.keys import Keys
        from selenium.webdriver.chrome.options import Options

        self.browser=webdriver.Chrome("notes/chromedriver.exe")
        self.username=#input('username:')
        self.password=#input('password:')


        self.comment =''
        self.browser.get('https://www.amazon.com/international-sales-offers/b/?ie=UTF8&node=15529609011&ref_=nav_cs_gb_intl_52df97a2eee74206a8343034e85cd058')
        time.sleep(3)
        self.browser.find_element_by_xpath("//*[@id='FilterItemView_sortOrder_dropdown']/div/span[2]/span/span/span/span").click()
        time.sleep(5)
        #self.browser.find_element_by_xpath("//*[@id='dropdown-3833758758044916_3']").click()
        self.browser.find_element_by_class_name("a-dropdown-link a-active").click()
        time.sleep(3)

    def dictionary_Notes(self):
        student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
        for key, value in student.items():
            print(key, value)

    def files_Notes(self):
        #File Objects
        ##The Basics:
        #f = open("test.txt", "r")
        #f = open("test.txt", "w")
        #f = open("test.txt", "a")
        #f = open("test.txt", "r+")
        #print(f.name)
        #print(f.mode)
        #f.close()

        ##Reading Files:
        #with open("test.txt", "r") as f:
            #pass

            ##Small Files:
            #f_contents = f.read()
            #print(f_contents)

            ##Big Files:
            #f_contents = f.readlines()
            #print(f_contents)

            ###With the extra lines:
            #f_contents = f.readline()
            #print(f_contents)
            #f_contents = f.readline()
            #print(f_contents)

            ###Without the extra lines:
            #f_contents = f.readline()
            #print(f_contents, end = '')
            #f_contents = f.readline()
            #print(f_contents, end = '')

            ###Iterating through the file:
            #for line in f:
                #print(line, end = '')

            ###Going Back....:
            #f_contents = f.read()
            #print(f_contents, end = '')

            ###Printing by characters:
            #f_contents = f.read(100)
            #print(f_contents, end = '')
            #f_contents = f.read(100)
            #print(f_contents, end = '')
            #f_contents = f.read(100)
            #print(f_contents, end = '')

            ###Iterating through small chunks:
            #size_to_read = 100
            #f_contents = f.read(size_to_read)
            #while len(f_contents) > 0:
                #print(f_contents)
                #f_contents = f.read(size_to_read)

            ###Iterating through small chunks, with 10 characters:
            #size_to_read = 10
            #f_contents = f.read(size_to_read)
            #print(f_contents, end = '')
            #f.seek(0)
            #f_contents = f.read(size_to_read)
            #print(f_contents, end = '')
            #print(f.tell())
            #while len(f_contents) > 0:
                #print(f_contents, end = '*')
                #f_contents = f.read(size_to_read)
        #print(f.mode)
        #print(f.closed)
        #print(f.read())


        ##Writing Files:
        ###The Error:
        #with open("test.txt", "r") as f:
            #f.write("Test")

        ###Writing Starts:
        #with open("test2.txt", "w") as f:
            #pass
            #f.write("Test")
            #f.seek(0)
            #f.write("Test")
            #f.seek("R")

        ##Copying Files:
        #with open("test.txt", "r") as rf:
            #with open("test_copy.txt", "w") as wf:
                #for line in rf:
                    #wf.write(line)

        #Copying the/your image:
        ###The Error
        #with open("bronx.jpg", "r") as rf:
            #with open("bronx_copy.jpg", "w") as wf:
                #for line in rf:
                    #wf.write(line)

        ###Copying the image starts, without chunks:
        #with open("bronx.jpg", "rb") as rf:
            #with open("bronx_copy.jpg", "wb") as wf:
                #for line in rf:
                    #wf.write(line)

        ###Copying the image with chunks:
        #with open("bronx.jpg", "rb") as rf:
            #with open("bronx_copy.jpg", "wb") as wf:
                #chunk_size = 4096
                #rf_chunk = rf.read(chunk_size)
                #while len(rf_chunk) > 0:
                    #wf.write(rf_chunk)
                    #rf_chunk = rf.read(chunk_size)

    def lists(self):
        # Empty Lists
        empty_list = []
        empty_list = list()

    def tuples(self):
        # Empty Tuples
        empty_tuple = ()
        empty_tuple = tuple()

    def sets(self):
        # Empty Sets
        empty_set = {} # This isn't right! It's a dict
        empty_set = set()

    def lists_Notes(self):
        # Mutable
        list_1 = ['History', 'Math', 'Physics', 'CompSci']
        list_2 = list_1

        print(list_1)
        print(list_2)

        # list_1[0] = 'Art'

        # print(list_1)
        # print(list_2)


        # Immutable
        # tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
        # tuple_2 = tuple_1

        # print(tuple_1)
        # print(tuple_2)

        # tuple_1[0] = 'Art'

        # print(tuple_1)
        # print(tuple_2)

        # Sets
        cs_courses = {'History', 'Math', 'Physics', 'CompSci'}

        print(cs_courses)


        # Empty Lists
        empty_list = []
        empty_list = list()

        # Empty Tuples
        empty_tuple = ()
        empty_tuple = tuple()

        # Empty Sets
        empty_set = {} # This isn't right! It's a dict
        empty_set = set()

    def random_Notes(self):
        ''' Super simple module to create basic random data for tutorials'''
        import random

        first_names = ['John', 'Jane', 'Corey', 'Travis', 'Dave', 'Kurt', 'Neil', 'Sam', 'Steve', 'Tom', 'James', 'Robert', 'Michael', 'Charles', 'Joe', 'Mary', 'Maggie', 'Nicole', 'Patricia', 'Linda', 'Barbara', 'Elizabeth', 'Laura', 'Jennifer', 'Maria']

        last_names = ['Smith', 'Doe', 'Jenkins', 'Robinson', 'Davis', 'Stuart', 'Jefferson', 'Jacobs', 'Wright', 'Patterson', 'Wilks', 'Arnold', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller', 'Wilson', 'Moore', 'Taylor', 'Anderson', 'Thomas', 'Jackson', 'White', 'Harris', 'Martin']

        street_names = ['Main', 'High', 'Pearl', 'Maple', 'Park', 'Oak', 'Pine', 'Cedar', 'Elm', 'Washington', 'Lake', 'Hill']

        fake_cities = ['Metropolis', 'Eerie', "King's Landing", 'Sunnydale', 'Bedrock', 'South Park', 'Atlantis', 'Mordor', 'Olympus', 'Dawnstar', 'Balmora', 'Gotham', 'Springfield', 'Quahog', 'Smalltown', 'Epicburg', 'Pythonville', 'Faketown', 'Westworld', 'Thundera', 'Vice City', 'Blackwater', 'Oldtown', 'Valyria', 'Winterfell', 'Braavos‎', 'Lakeview']

        states = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY']

        for num in range(100):
            first = random.choice(first_names)
            last = random.choice(last_names)

            phone = f'{random.randint(100, 999)}-555-{random.randint(1000,9999)}'

            street_num = random.randint(100, 999)
            street = random.choice(street_names)
            city = random.choice(fake_cities)
            state = random.choice(states)
            zip_code = random.randint(10000, 99999)
            address = f'{street_num} {street} St., {city} {state} {zip_code}'

            email = first.lower() + last.lower() + '@bogusemail.com'

            print(f'{first} {last}\n{phone}\n{address}\n{email}\n')

    def setuptools_Notes(self):
        import setuptools
        setuptools.setup(
            name = 'socialmediascraper',
            version = '0.0-dev',
            description = 'A social media scraper',
            packages = ['socialmediascraper'],
            install_requires = ['requests', 'lxml', 'beautifulsoup4'],
            entry_points = {
                'console_scripts': [
                    'smscrape = socialmediascraper.cli:main',
                ],
            },
        )

    def time_hak(self):
        yesterday = datetime.strftime(datetime.now() - timedelta(1), '%Y-%m-%d')
        tomorrow = datetime.strftime(datetime.now() + timedelta(1), '%Y-%m-%d')
        today = datetime.strftime(datetime.now(), '%Y-%m-%d')

        last_3_hour = datetime.strftime(datetime.now() - timedelta(hours = 3), '%Y-%m-%d %H:%M:%S')
        now = datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')
        print(yesterday)
        print(tomorrow)
        print(today)

    def flask_Notes(self):
        from flask import Flask
        app = Flask(__name__)

        @app.route("/")
        def hello():
            return "Hello World!"

        @app.route("/about")
        def about():
            return "About Page"

        if __name__ == "__main__":
            app.run()

    def slicing(self):
        my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        # list[start:end:step]
        # print my_list[::-1]

        sample_url = 'http://coreyms.com'
        # Reverse the url
        # print sample_url[::-1]

        # # Get the top level domain
        # print sample_url[-4:]

        # # Print the url without the http://
        # print sample_url[7:]

        # # Print the url without the http:// or the top level domain
        print(sample_url[7:-4])



if __name__ == '__main__':
    pnotes = PythonNotes()

    pnotes.fibonacci2(int(sys.argv[1]))
    pnotes.fibonacci2(int(sys.argv[1]))