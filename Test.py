#Простенький скрипт по решению теста на сервисе вуза.



from selenium import webdriver
import time
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import lxml
import requests
from selenium.webdriver.common.by import By
import numpy as np
import pandas as pd
import scipy.stats as sts
from lxml import etree


#options

options = webdriver.ChromeOptions()
useragent = UserAgent()

options.add_argument(f"user-agent={useragent}")
#
# set proxy
# options.add_argument("--proxy-server=216.189.154.71:80")

###########
url = "https://campus.fa.ru/login/index.php"

useragent = UserAgent()

driver = webdriver.Chrome(
    executable_path=r"C:\Users\Devi\PycharmProjects\RAR\rar\Chromedriver\chromedriver.exe",
    options=options
)

login = str(input())
password = str(input())

try:
    driver.get(url=url)
    time.sleep(1)

    Login_input = driver.find_element_by_id('username')
    Login_input.clear()
    Login_input.send_keys(login)
    time.sleep(1)

    Password_input = driver.find_element_by_id("password")
    Password_input.clear()
    Password_input.send_keys(password)

    time.sleep(1)
    login_button = driver.find_element_by_id('loginbtn').click()

    driver.get(url='https://campus.fa.ru/mod/quiz/view.php?id=89602')

    time.sleep(1)

    try:
        start = driver.find_element_by_xpath('//button[contains(text(), "Начать тестирование")]').click()
        time.sleep(1)
        start_ok = driver.find_element_by_id('id_submitbutton').click()
        time.sleep(1)
    except Exception:
        try:
            start = driver.find_element_by_xpath('//button[contains(text(), "Пройти тест заново")]').click()
            time.sleep(1)
            start_ok = driver.find_element_by_id('id_submitbutton').click()
            time.sleep(1)
        except Exception:
            start = driver.find_element_by_xpath('//button[contains(text(), "Продолжить последнюю попытку")]').click()
            time.sleep(1)
    src = driver.page_source


    soup = BeautifulSoup(src, "lxml")
    task_read = soup.find("div", class_="qtext").find("p").text
    print(task_read)
    task_read.replace(" ","")
    a = []
    flag = 0
    for i in task_read:

        if i == '{':
            flag = 1
        elif i == '}':
            flag = 0
            a.append(i)

        if flag == 1:
            a.append(i)
    a = ''.join(a)
    b = a.split('}')
    d = list(map(float,b[1].replace('NA','-1').replace('{','').replace(',','.').replace(' ','').split(';')))
    e = list(map(float,b[2].replace('{','').replace(',','.').replace(' ','').split(';')))
    c = list([i for i in range(1,len(e)+1)])

    df = pd.DataFrame({'Дата': c, 'Цена': d, 'Объём': e})
    df['Цена'].replace(0, np.nan, inplace=True)
    df.dropna(axis=0,inplace=True)
    df['Цена'].replace(-1, np.nan, inplace=True)
    df.dropna(axis=0,inplace=True)
    df['Объём'].replace(0.000, np.nan, inplace=True)
    df.dropna(axis=0,inplace=True)

    id_range = list([i for i in range(1,df.shape[0]+1)])
    df['Дата'] = id_range
    print(df)

    #Запись ответов

    t6 = int(df.shape[0])
    t7_s = soup.find(class_='filter_mathjaxloader_equation').find('span', class_="nolink")
    t7_s = t7_s.text
    t7_sn = ''
    for i in t7_s:
        if i in '1234567890':
            t7_sn+= i
    t7_sn = int(t7_sn)-1

    t7_1 = df.iloc[t7_sn]['Дата']

    t7_2 = df.iloc[t7_sn]['Цена']

    t7_3 = df.iloc[t7_sn]['Объём']

    t8 = df['Цена'].mean()
    t9 = df['Объём'].mean()
    t10 = df['Цена'].std()
    t11 = df['Объём'].std()
    t12 = t10/(t6)**0.5
    t13 = df['Цена'].min()
    t14 = df['Объём'].max()
    t15 = sts.kurtosis(df['Цена'],bias=False)

#     #Ввод данных
    id_d = soup.find(class_='subq accesshide').get('for')
    id_d = id_d[0:7]

    Input_6 = driver.find_element_by_xpath(f'//*[@id="{id_d}:1_0_0"]').send_keys(t6)
    time.sleep(0.5)
    Input_7_1 = driver.find_element_by_xpath(f'//*[@id="{id_d}:1_1_0"]').send_keys(t7_1)
    time.sleep(0.5)
    Input_7_2 = driver.find_element_by_xpath(f'//*[@id="{id_d}:1_1_1"]').send_keys(t7_2)
    time.sleep(0.5)
    Input_7_3 = driver.find_element_by_xpath(f'//*[@id="{id_d}:1_1_2"]').send_keys(t7_3)
    time.sleep(0.5)
    Input_8 = driver.find_element_by_xpath(f'//*[@id="{id_d}:1_2_0"]').send_keys(t8)
    time.sleep(0.5)
    Input_9 = driver.find_element_by_xpath(f'//*[@id="{id_d}:1_3_0"]').send_keys(t9)
    time.sleep(0.5)
    Input_10 = driver.find_element_by_xpath(f'//*[@id="{id_d}:1_4_0"]').send_keys(t10)
    time.sleep(0.5)
    Input_11 = driver.find_element_by_xpath(f'//*[@id="{id_d}:1_5_0"]').send_keys(t11)
    time.sleep(0.5)
    Input_12 = driver.find_element_by_xpath(f'//*[@id="{id_d}:1_6_0"]').send_keys(t12)
    time.sleep(0.5)
    Input_13 = driver.find_element_by_xpath(f'//*[@id="{id_d}:1_7_0"]').send_keys(t13)
    time.sleep(0.5)
    Input_14 = driver.find_element_by_xpath(f'//*[@id="{id_d}:1_8_0"]').send_keys(t14)
    time.sleep(0.5)
    Input_15 = driver.find_element_by_xpath(f'//*[@id="{id_d}:1_9_0"]').send_keys(t15)
    time.sleep(0.5)

    src = driver.page_source
    soup = BeautifulSoup(src, "lxml")

    id_next = soup.find(class_='submitbtns').find('input').get('id')
    print(id_next)
    driver.find_element_by_id(f'{id_next}').click()
    time.sleep(1)

    src = driver.page_source
    soup = BeautifulSoup(src, "lxml")

    id_next2 = soup.find(class_='mod_quiz-next-nav btn btn-primary').get('id')
    print(id_next2)
    driver.find_element_by_id(f'{id_next2}').click()
    time.sleep(1)

    src = driver.page_source
    soup = BeautifulSoup(src, "lxml")

    driver.find_element_by_xpath('//button[contains(text(), "Отправить всё и завершить тест")]').click()
    time.sleep(1)

    src = driver.page_source
    soup = BeautifulSoup(src, "lxml")

    id_next3 = soup.find('input', class_='btn btn-primary').get('id')
    last_s = driver.find_elements_by_id(f'{id_next3}')
    last_s[0].click()

    time.sleep(360)



except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
