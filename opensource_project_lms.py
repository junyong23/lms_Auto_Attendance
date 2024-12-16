from telnetlib import EC
from datetime import datetime

import uc
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

from selenium.webdriver.support.wait import WebDriverWait

options = Options()
options.add_argument("--start-maximized")
#options.add_argument("user-data-dir=C:\\Users\\junyo\\OneDrive\\바탕 화면\\Test")
#options.add_argument("disable-blink-features=AutomationControlled")
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)

driver.get('https://lms.hanbat.ac.kr/')

time.sleep(2)

id_btn = driver.find_element(By.ID, 'login_user_id')
id_btn.send_keys('20232071')

pw_btn = driver.find_element(By.ID, 'login_user_password')
pw_btn.click()
pw_btn.send_keys('cho182931!')

login_btn = driver.find_element(By.CLASS_NAME, 'login_btn')
login_btn.click()

time.sleep(1)
calen_btn = driver.find_element(By.ID, 'global_nav_calendar_link')
calen_btn.click()

time.sleep(1)

now = datetime.now()
month = now.month
file_name = f"C:/Users/junyo/OneDrive/바탕 화면/{month}월 일정.txt"
file_header = f"{month}월의 과제 및 일정 입니다.\n\n"

f = open(file_name, "w")
f.write(file_header)

test = driver.find_elements(By.CLASS_NAME, "fc-event-container")

j = 1
for i in test:
    f.write(str(j) + ". -------------------------\n")
    title = i.text
    print(title+"\n")
    f.write(title)
    f.write("\n----------------------------\n\n\n")
    j = j + 1

f.close()