from bs4 import BeautifulSoup
import urllib.request as req
from selenium import webdriver
from selenium.webdriver.support.ui import Select

def PageReader(html):
    soup = BeautifulSoup(html, 'html.parser')
    info = soup.select(".default_tb > tbody > tr > td")
    lawlist = []
    for i in range(0,len(info),5):
        if info[i+1].string == "국가기술표준원" or  info[i+1].string == "특허청":
            continue
        elif  info[i+4].string != "법":
            continue
        m=[info[i+1].string, info[i+2].string.strip(), info[i+3].string]
        lawlist.append(m)
    return lawlist

driver = webdriver.Chrome(r"C:\Users\traya\Desktop\chromedriver_win32\chromedriver")
driver.implicitly_wait(3)

url = 'http://likms.assembly.go.kr/bill/main.do'
driver.get(url)

# 상세검색 -> 산중위 선택 -> 검색버튼
driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div[1]/ul/li[2]/a").click()
driver.find_element_by_xpath("/html/body/div/div[2]/div[1]/ul/li[2]/a").click()
select = Select(driver.find_element_by_xpath('//*[@id="chargeCommitteeName"]'))
select.select_by_visible_text("산업통상자원중소벤처기업위원회")
driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/div[2]/button[1]").click()

# 100개씩 보기
select = Select(driver.find_element_by_xpath('//*[@id="pageSizeOption"]'))
select.select_by_visible_text("100")

# 하나 들어왔을때
def one_law_reader(html):
    soup = BeautifulSoup(html, 'html.parser')
    number = soup.select(.table)


body > div > div.contentWrap > div.subContents > div > div:nth-child(3) > div.tableCol01 > table > tbody > tr > td:nth-child(1)