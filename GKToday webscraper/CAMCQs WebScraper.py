import urllib.request as urllib2
import requests
import xlwt
from xlwt import Workbook
from bs4 import BeautifulSoup
from lxml import html
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


loc = ("C:/Users/Omkar Jawaji/Downloads/Bidus/que.xlsx")
# Workbook is created
wb = Workbook()
# add_sheet is used to create sheet.
sheet = wb.add_sheet('Sheet', cell_overwrite_ok=True)


url = "https://www.gktoday.in/category/gk-questions/"
page = urllib2.urlopen(url)
soup = BeautifulSoup(page, 'html.parser')

latest_pgn = soup.find('a', attrs={'class': 'last'}).text.strip()
pgn = int(latest_pgn)

list_ques = list()
date = ""
i = 0
z = 0
for pgn in range(210, 288):
    # print(pgn)
    list_ques = list()
    pg_url = "https://www.gktoday.in/category/gk-questions/page/" + \
        str(pgn)
    page = urllib2.urlopen(pg_url)
    soup1 = BeautifulSoup(page, 'html.parser')
    date = soup1.findAll('span', attrs={'class': 'meta_date'})
    # print("")
    # print(date)
    # print("")
    for i in range(0, 5):
        sheet.write(z, 0, str(date[i].text))
        format_date = date[i].text.strip().replace(",", "").replace(" ", "-")
        print(format_date)
        ques_url = "https://www.gktoday.in/todays-gk-questions-static-gk-gs-" + format_date
        page = urllib2.urlopen(ques_url)
        soup2 = BeautifulSoup(page, 'html.parser')

        list_ques = soup2.findAll(
            'div', attrs={'class': 'ques_txt'})
        k = 0
        list_ans = soup2.select("div[class^=question_list]")
        # print(len(list_ans))
        # print(list_ques)
        for j in range(0, len(list_ans)):
            sheet.write(z, j+1, "Q"+str(j+1)+")"+list_ques[j].text.strip())
            list_opt = list_ans[j].findAll('label')
            string = ""
            num = str(list_opt).count("label")
            for l in range(0, int(num/2)):
                # print(list_opt[l].text.strip())
                # print("")
                string = string + str(l+1) + ")" + \
                    str(list_opt[l].text.strip())+" "
                # print(string)
                # print("")
                sheet.write(z+1, j+1, string)
        z = z+2
wb.save('xlwt bidusques.xls')
