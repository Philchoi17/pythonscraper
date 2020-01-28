from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import csv
import requests
from selenium.common.exceptions import NoSuchElementException
from pprint import pprint


class data_scraper(object):
    def __init__(self):
        path_to_chromedriver = '/usr/local/bin/chromedriver'
        self.browser = webdriver.Chrome(executable_path = path_to_chromedriver)
        chrome_options = webdriver.ChromeOptions()
        prefs = {"profile.managed_default_content_settings.images": 2}
        chrome_options.add_experimental_option("prefs", prefs)
        self.browser = webdriver.Chrome(options = chrome_options)

    def login_process(self):
        # login url here!
        login_url = 'url to login'
        self.browser.get(login_url) 
        #successfully navigated to URL_1
        
        # open dev tools ( inspector ) and located by id or x path the username input
        elem = self.browser.find_element_by_id("id username input")
        elem.clear()
        # username text here
        elem.send_keys("username")

        # sameas above but with password input
        elem = self.browser.find_element_by_id("id password input")
        elem.clear()
        # password text here
        elem.send_keys("password")
        self.browser.find_element_by_xpath("path to login button").click()
        #successfully entered URL_2 

    def query(self):
        cno_num = 1
        info_arr = []
        with open('data_name.csv', 'w') as csvfile:
            filewriter = csv.writer(csvfile, delimiter=',',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            filewriter.writerow(['headers'])
            while cno_num < 10:
                info_arr = []
                # switch url to a domain you want to scrape!!
                url = 'https://boxrec.com/en/proboxer/'
                self.browser.get(url + str(cno_num))
                html = self.browser.page_source
                
                # initialize soup parser here
                soup = BeautifulSoup(html, 'html.parser')
                try:
                    # located data within the source code here using the soup.find or however
                    info_arr.append(soup.select('title'))
                    #things you want to do and make array
                    print(info_arr)
                    # some conditional to make sure enough data is there
                    if len(info_arr) == 1:
                        filewriter.writerow(info_arr)
                    else:
                        pass
                except:
                    # good to catch any errors
                    print('here' + str(cno_num))
                    pass
                cno_num+=1
        
data_scraper = data_scraper()
# data_scraper.login_process()
data_scraper.query()