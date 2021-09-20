import urllib.request as urllib2
import requests
import xlwt
from xlwt import Workbook
from bs4 import BeautifulSoup
from lxml import html
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

links = list()
# Workbook is created
wb = Workbook()
# add_sheet is used to create sheet.
sheet = wb.add_sheet('Sheet1', cell_overwrite_ok=True)

for x in range(1500, 1575):
    print(x)
    url = "https://www.gktoday.in/current-affairs/page/"+str(x)
    page = urllib2.urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')

    cnt = 0
    list_ans = soup.find(
        'div', attrs={'class': 'posts-listing'})
    list_que = list_ans.findAll('h1')
    for i in list_que:
        for a in i.findAll('a', href=True):
            links.append(a['href'])
            for l in links:
                cnt = cnt + 1
                data_page = urllib2.urlopen(l)
                soup2 = BeautifulSoup(data_page, 'html.parser')
                k = soup2.find('div', attrs={
                    'class': 'inside_post column content_width'})
                # print(len(k.text.strip()))
                '''
                pos = k.find("Month:")
                print(pos)
                k = k[:pos]
                '''
                sheet.write(cnt, 0, k.text.strip())
    wb.save('xlwt bidusquestions4.xls')
wb.save('xlwt bidusquestions4.xls')

'''
& "C:/Users/Omkar Jawaji/AppData/Local/Programs/Python/Python38/python.exe" "c:/Users/Omkar Jawaji/Downloads/Bidus/Webscrapping/500to600.py"
& "C:/Users/Omkar Jawaji/AppData/Local/Programs/Python/Python38/python.exe" "c:/Users/Omkar Jawaji/Downloads/Bidus/Webscrapping/600to700.py"
& "C:/Users/Omkar Jawaji/AppData/Local/Programs/Python/Python38/python.exe" "c:/Users/Omkar Jawaji/Downloads/Bidus/Webscrapping/700to800.py"
'''
