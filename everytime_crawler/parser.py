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

browser.find_element_by_css_selector("#menu > li:nth-child(3) > a").click()
time.sleep(2)

SCROLL_PAUSE_TIME = 0.5
# Get scroll height
last_height = browser.execute_script("return document.body.scrollHeight")
while True:
    # Scroll down to bottom
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)
    # Calculate new scroll height and compare with last scroll height
    new_height = browser.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

reviews = browser.find_elements_by_class_name("article")
time.sleep(1)
i = 0
print(len(reviews))

while i < len(reviews):
    # for review in reviews:
    reviews[i].send_keys(Keys.CONTROL + '\n')
    browser.switch_to.window(browser.window_handles[1])
    wait = WebDriverWait(browser, 10)
    wait.until(EC.presence_of_element_located((By.ID, "container")))
    
    #여기서부터 정보 가져옴
        
    req = browser.page_source
    soup = BeautifulSoup(req,'html.parser')
    #강의명
    coursename_list = soup.select("#container > div.side.head > h2")
    for coursename in coursename_list:
        a = coursename.text
        
    #교수명
    prof_list = soup.select('#container > div.side.head > p:nth-child(2) > span')
    for prof in prof_list:
        b = prof.text
    
    #별점
    star_list = soup.select('#container > div.side.article > div.rating > div.rate > span > span.value')
    for star in star_list:
        c = star.text

    #후기
    comment_list = soup.find_all('p','text')
    comments = []
    for comment in comment_list:
        d = comment.get_text()
        comments.append(d)

    reviewdatas = [a,b,c,comments]
    browser.close()
    browser.switch_to.window(browser.window_handles[0])
    i+=1
    time.sleep(2)

    print(reviewdatas)