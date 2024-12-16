from telnetlib import EC
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

from selenium.webdriver.support.wait import WebDriverWait

options = Options()
options.add_argument("--start-maximized")
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)

driver.get('https://lms.hanbat.ac.kr/')

time.sleep(2)

id_box = driver.find_element(By.ID, 'login_user_id')
id_box.send_keys('20232071')

pw_box = driver.find_element(By.ID, 'login_user_password')
pw_box.click()
pw_box.send_keys('cho182931!')
login_btn = driver.find_element(By.CLASS_NAME, 'login_btn')
login_btn.click()

time.sleep(1)
calen_btn = driver.find_element(By.ID, 'global_nav_calendar_link')
calen_btn.click()

time.sleep(1)

now = datetime.now()
month = now.month
file_name = f"C:/Users/junyo/OneDrive/바탕 화면/{month}월 일정.txt"
file_header = f"{month}월의 일정 입니다.\n"

f = open(file_name, "w")
f.write(file_header)
if(month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12):
    for i in range(1, 32, 1):
        f.write("Hello")
f.close()


time.sleep(15)
