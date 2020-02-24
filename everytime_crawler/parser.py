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

browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

while True:
    reviews = browser.find_elements_by_xpath("//*[@id='container']/div[2]/div/a")
    for review in reviews:
        review.send_keys(Keys.ENTER)
        wait = WebDriverWait(browser, 10)
        wait.until(EC.presence_of_element_located((By.ID, "container")))
        coursename = review.find_element_by_css_selector('#container > div.side.head > h2')
        print(coursename)