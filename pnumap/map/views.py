from django.shortcuts import render, redirect, get_object_or_404
from .forms import BlogForm
from .models import Blog, TempCrawlData
from django.http import HttpResponse, JsonResponse
import json

from .models import Blog, ReviewData, Course, Professor, TempCrawlData
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# from bs4 import BeautifulSoup
# import time

# def coursedata(request):
#     browser = webdriver.Chrome(r"C:\Users\USER\Desktop\likelion\likelion8th\E-Moboo\chromedriver_win32\chromedriver.exe")
#     browser.get('https://everytime.kr/login')
#     time.sleep(1)

#     login = browser.find_element_by_name('userid')
#     login.send_keys('etcheef')
#     login = browser.find_element_by_name('password')
#     login.send_keys('Rimee202=')
#     login.send_keys(Keys.RETURN)
#     time.sleep(1)
#     browser.find_element_by_css_selector("#menu > li:nth-child(2) > a").click()
#     time.sleep(1)
#     browser.find_element_by_xpath("//*[@id='container']/ul/li[1]").click()
#     browser.find_element_by_css_selector("#subjects")
#     time.sleep(5)
#     close = browser.find_element_by_xpath("//*[@id='sheet']/ul/li[3]/a").click()

#     time.sleep(2)
#     temp_list = list()
#     for i in range(20):
#         trs = browser.find_elements_by_css_selector("#subjects > div.list > table > tbody > tr")
#         browser.execute_script("arguments[0].scrollIntoView(true);", trs[-1])

#     for tr in trs[:100]:
#         # print(tr.text)
#         temp_list.append((tr.text).split(" "))
    
#     del temp_list[0][0]
#     for i in temp_list:
#         print(i)
#         TempCrawlData.objects.create(buildingnum = i[8], profname = i[5], coursename= i[2])
#     return redirect('main')

# def reviewdata(request):
#     browser = webdriver.Chrome(r"C:\Users\USER\Desktop\likelion\likelion8th\E-Moboo\chromedriver_win32\chromedriver.exe")
#     browser.get('https://everytime.kr/login')
#     time.sleep(1)

#     login = browser.find_element_by_name('userid')
#     login.send_keys('etcheef')
#     login = browser.find_element_by_name('password')
#     login.send_keys('Rimee202=')
#     login.send_keys(Keys.RETURN)

#     browser.find_element_by_css_selector("#menu > li:nth-child(3) > a").click()
#     time.sleep(2)

#     SCROLL_PAUSE_TIME = 0.5
#     last_height = browser.execute_script("return document.body.scrollHeight")
#     while True:
#         browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#         time.sleep(SCROLL_PAUSE_TIME)
#         new_height = browser.execute_script("return document.body.scrollHeight")
#         if new_height == last_height:
#             break
#         last_height = new_height

#     reviews = browser.find_elements_by_class_name("article")
#     time.sleep(1)
#     i = 0

#     while i < len(reviews):
#         reviews[i].send_keys(Keys.CONTROL + '\n')
#         browser.switch_to.window(browser.window_handles[1])
#         wait = WebDriverWait(browser, 10)
#         wait.until(EC.presence_of_element_located((By.ID, "container")))
    
#         #여기서부터 정보 가져옴
#         req = browser.page_source
#         soup = BeautifulSoup(req,'html.parser')
#         coursename_list = soup.select("#container > div.side.head > h2")
#         for coursename in coursename_list:
#             a = coursename.text
        
#         prof_list = soup.select('#container > div.side.head > p:nth-child(2) > span')
#         for prof in prof_list:
#             b = prof.text
    
#         star_list = soup.select('#container > div.side.article > div.rating > div.rate > span > span.value')
#         for star in star_list:
#             c = star.text

#         #후기
#         comment_list = soup.find_all('p','text')
#         comments = []
#         for comment in comment_list:
#             d = comment.get_text()
#             comments.append(d)

#         Professor.objects.create(name=b)
#         Course.objects.create(course=a)
#         ReviewData.objects.create(star=c, review=d)

#         browser.close()
#         browser.switch_to.window(browser.window_handles[0])
#         i+=1
#         time.sleep(2)
#     return render(request)

def main(request):
    return render(request, "main.html")

def search(request):
    context={"msg": "hello chihun"}
    return HttpResponse(json.dumps(context), content_type='application/json')

def score(request,flag):
    print(flag)
    if flag == "score_up":
        context ={'msg': 'up'}
    else:
        context ={'msg': 'down'}
    return HttpResponse(json.dumps(context), content_type='application/json')


def index(request):
    buildings = Blog.objects.all()
    return render(request, 'index.html', {'buildings':buildings})

def write(request):
    blogform = BlogForm(request.POST)
    if blogform.is_valid():
        blogform.save()
        return redirect('main')
    blogform = BlogForm()
    return render(request, 'write.html', {'blogform':blogform})

def detail(request, building_id):
    building = get_object_or_404(Blog, id=building_id)
    return render(request, 'detail.html', {'building':building})

def update(request, building_id):
    building_update = get_object_or_404(Blog, id=building_id)
    if request.method == "POST":
        blogform = BlogForm(request.POST, instance=building_update)
        if blogform.is_valid():
            blogform.save()
            return redirect('main')
    blogform = BlogForm(instance=building_update)
    return render(request, 'write.html', {'blogform':blogform})

def delete(request,building_id):
    building_delete = get_object_or_404(Blog, id=building_id)
    building_delete.delete()
    return redirect('main')


def building_info(request,building_id):
    dataset = TempCrawlData.objects.filter(buildingnum__contains='-')
    building_data = dataset.filter(buildingnum__startswith=building_id)
    return render(request, 'main.html', {'building_data':building_data})




def building_info_detail(request, lec_id):
    data = TempCrawlData.objects.get(id=lec_id)
    return render(request, 'main.html' , {'lec_data':data})