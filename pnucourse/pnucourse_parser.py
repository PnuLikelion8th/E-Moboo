from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

browser = webdriver.Chrome(r"C:\Users\USER\Desktop\likelion\likelion8th\E-Moboo\chromedriver_win32\chromedriver.exe")
browser.get('https://everytime.kr/login')
time.sleep(1)

login = browser.find_element_by_name('userid')
login.send_keys('etcheef')
login = browser.find_element_by_name('password')
login.send_keys('Rimee202=')
login.send_keys(Keys.RETURN)
time.sleep(1)
browser.find_element_by_css_selector("#menu > li:nth-child(2) > a").click()
time.sleep(1)
browser.find_element_by_xpath("//*[@id='container']/ul/li[1]").click()
browser.find_element_by_css_selector("#subjects")
time.sleep(5)
close = browser.find_element_by_xpath("//*[@id='sheet']/ul/li[3]/a").click()

time.sleep(2)
total_list= list()
while True:
    trs = browser.find_elements_by_css_selector("#subjects > div.list > table > tbody > tr")
    browser.execute_script("arguments[0].scrollIntoView(true);", trs[-1])

    for tr in trs:
        # print(tr.text)
        total_list.append((tr.text).split(" "))
        print("*"*50)
        print(total_list)
        print("*"*50)


        total_list[0][0].remove()
        # tds = browser.find_elements_by_css_selector('#subjects > div.list > table > tbody > tr > td')
        # i=0
        # for td in tds:
        #     if td.text=="":
        #         print("악")
        #     else:
        #         print(td.text)

# SCROLL_PAUSE_TIME = 0.5
# # Get scroll height
# last_height = browser.execute_script("return document.body.scrollHeight")
# while True:
#     # Scroll down to bottom
#     browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     # Wait to load page
#     time.sleep(SCROLL_PAUSE_TIME)
#     # Calculate new scroll height and compare with last scroll h`eight
#     new_height = browser.execute_script("return document.body.scrollHeight")
#     if new_height == last_height:
#         break
#     last_height = new_height

# # req = browser.page_source
# # soup = BeautifulSoup(req,'html.parser')
# # trs = soup.find_all('tr')

# # print (trs[1])

# # subjects = Select(browser.find_element_by_id("subject_is"))
# # #교양선택/일반선택
# # subjects.select_by_visible_text("교양선택및일반선택(일반교양)")
# # time.sleep(1)
# # refines = browser.find_elements_by_xpath("//*[@id='refinementAndMajor']/option")
# # i=0
# # for i in range(len(refines)):
# #     refines[i].click()
# #     search = browser.find_element_by_id("search")
# #     search.click()
# #     time.sleep(2)

# #     req = browser.page_source
# #     soup = BeautifulSoup(req,'html.parser')
# #     table_div = soup.find("div")['table-responsive']
# #     trs = table_div.find_all('tr')

# #     print(trs[1])`