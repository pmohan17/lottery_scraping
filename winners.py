
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from random import randint
from urllib.request import urlopen
import requests, re
from bs4 import BeautifulSoup
import csv
session = requests.Session()
hdr = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}
url= "https://nylottery.ny.gov/winners-wall"
req = session.get(url, headers=hdr)



options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
driver = webdriver.Chrome('C:/Users/13526/Documents/python/lottery_winners/chromedriver_win32/chromedriver.exe', chrome_options=options)
driver.get('https://nylottery.ny.gov/winners-wall');

csvfile = open("lottery.csv", 'w', newline='', encoding='utf-8')
c = csv.writer(csvfile, delimiter=',')

for n in range(17):
    driver.find_element_by_css_selector(".pagination .next").click();
    s = randint(1, 10)
    time.sleep(s)
html = driver.page_source
bsObj = BeautifulSoup(html, "html5lib")
alist=[]
hreflist=[]
winner_details = []
container = bsObj.find( "div", {"class":"main-container"} )
winner_list = container.findAll("div", {"class":"winner-item"} )
for winner in winner_list:
    alist.append(winner.find('a'))
for a in alist:
    hreflist.append(a.get('href'))

c.writerow(hreflist)

def get_winner_details(winner_list):
    for winner in winner_list:
        # new_url = "https://nylottery.ny.gov" + winner
        html =  driver.page_source
        bsObj = BeautifulSoup(html, "html5lib")
        headline=bsObj.find('h2')
        name=bsObj.find('h3')
        winner_details = [headline, name]
        row=[]
        for detail in winner_details:
            try:
                row.append( detail.get_text() )
            except AttributeError:
                row.append( "None" )
        c.writerow(row)

get_winner_details(winner_list)
csvfile.close()

driver.quit()
