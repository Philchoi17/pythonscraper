from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import csv
import requests
from selenium.common.exceptions import NoSuchElementException


class rei_scraper(object):
    def __init__(self):
        path_to_chromedriver = 'path to chromedriver'
        self.browser = webdriver.Chrome(executable_path = path_to_chromedriver)
        chrome_options = webdriver.ChromeOptions()
        prefs = {"profile.managed_default_content_settings.images": 2}
        chrome_options.add_experimental_option("prefs", prefs)
        self.browser = webdriver.Chrome(options = chrome_options)

    def login_process(self):
        login_url = 'url to login'
        self.browser.get(login_url) 
        #successfully navigated to URL_1

        elem = self.browser.find_element_by_id("id username input")
        elem.clear()
        elem.send_keys("username")

        elem = self.browser.find_element_by_id("id password input")
        elem.clear()
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
            while cno_num < 90000:
                info_arr = []
                self.browser.get('url' + str(cno_num))
                # html = self.browser.page_source
                # soup = BeautifulSoup(html, 'html.parser')
                try:
                    #things you want to do and make array
                    
                    if len(info_arr) == 100:
                        print(info_arr)
                        filewriter.writerow(info_arr)
                    else:
                        pass
                except:
                    print('here' + str(cno_num))
                    pass
                cno_num+=1
        
rei_scraper = rei_scraper()
rei_scraper.login_process()
rei_scraper.query()