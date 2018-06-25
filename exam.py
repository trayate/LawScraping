from bs4 import BeautifulSoup
import requests
import urllib.request as req
from selenium import webdriver
from selenium.webdriver.support.ui import Select

url = "http://likms.assembly.go.kr/bill/billDetail.do?billId=PRC_F1S6W1V0X1U9Z1Q7B2G8Q3W3O7C6A3"

def one_law_reader(html):
    req = requests.get(html)
    html= req.text
    soup = BeautifulSoup(html, 'html.parser')

    # 의안접수정보

    #의안번호
    number = soup.select("div.tableCol01 > table > tbody > tr > td")[0].text
    #제안일자
    when = soup.select("div.tableCol01 > table > tbody > tr > td")[1].text
    #제안자
    who = soup.select("div.tableCol01 > table > tbody > tr > td")[2].text.rstrip()

    # 소관위 심사정보


    print(who)


one_law_reader(url)
##
#
#

####
