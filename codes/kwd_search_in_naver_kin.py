
from bs4 import BeautifulSoup
from datetime import datetime, date, timedelta
import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

import openpyxl
from openpyxl.styles import PatternFill, Color
from openpyxl import Workbook
from random import *

"""
It is strongly recommended to install the "tor" in advance.
More details to see: https://www.torproject.org/zh-CN/download/.
"""
path = r"E:\Naver_kin\geckodriver.exe"

def firefox_dirver(path, is_tor=True):
    
    # firefox profile settings
    profile = webdriver.FirefoxProfile()

    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0' # user agent can be changed
    profile.set_preference('general.useragent.override', user_agent)
    profile.set_preference('permissions.default.image', 2)
    
    if is_tor:
        profile.set_preference("network.proxy.type", 1) # for tor
        profile.set_preference("network.proxy.socks", "127.0.0.1") # for tor
        profile.set_preference("network.proxy.socks_port", 9050) # for tor
        profile.set_preference('dom.ipc.plugins.enabled.npswf32.dll', 'false')#Windows
        
    driver = webdriver.Firefox(firefox_profile=profile, executable_path=path)
    
    return driver

def get_keyword(kwd):
    return kwd.replace(" ", "%20")

def sort_type(x):
    if x == 'v':
        return 'vcount'
    elif x == 'd':
        return 'date'
    else:
        return 'none'
    
def time_type(time=(2010, 1, 1)):
    year, month, day = time
    year = str(year)
    if month < 10: month = '0' + str(month) 
    else: month = str(month)
    if day < 10: day = '0' + str(day)
    else: day = str(day)
    return '.'.join([year, month, day])
  
  
def get_url(kwd, start_time, end_time, sort='d', section='qna', dirid='110805'):
    query = 'query=' + get_keyword(kwd)
    period = '|'.join([time_type(x) for x in [start_time, end_time]])
    sort = 'sort=' + sort_type(sort)
    section = 'section=' + section
    dirid = 'dirId=' + dirid
    url = 'https://kin.naver.com/search/list.nhn?' + '&'.join([query, period, sort, section, dirid])
    return url

def search_pages(kwd, url_0, page_index=1):
    file = open("result/url_list" + "_" + kwd.replace(' ', '+') + ".txt", 'a+')
    page_url = []
    while True:
        url_p = url_0 + '&page=' + str(page_index)
        time.sleep(uniform(1, 3))
        driver.implicitly_wait(20)
        driver.get(url_p)
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        tags = soup.find_all('a', class_="_nclicks:qna.txt _searchListTitleAnchor")
        for tag in tags:
            url = str(tag).split(' ')[3]
            url = url.replace('href=', "")
            url = url.replace('"', "")
            url = url.replace('amp;', '')
            page_url.append(url)
            file.write(url + "\n")

        post_number = driver.find_element_by_class_name('number').text
        post_number = str(post_number).replace("(", "")
        post_number = str(post_number).replace(")", "")
    
        current_number = post_number.split('/')[0].split('-')[1]
        current_number = current_number.replace(',', '')
        total_number = post_number.split('/')[1]
        total_number = total_number.replace(',', '')

        if int(current_number) == int(total_number):
            break
        elif int(current_number) > 1000:
            print(' The numbers of accessible Q&As cannot exceed 1000.')
            break
        else:
            page_index += 1
        
    file.close()
    return page_url

###############################################################################
if __name__ == '__main__':
    path = r".\geckodriver.exe"
    is_tor = False
    driver = firefox_dirver(path, is_tor)
    kwd = ''
    start_time, end_time = (2010,1,1), (2010,2,1)
    url = get_url(kwd, start_time, end_time)
    page_url = search_pages(kwd, url, page_index=1)
    
    
    
    
