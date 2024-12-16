from telnetlib import EC

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

firstclass_btn = driver.find_element(By.CLASS_NAME, 'ic-DashboardCard')
firstclass_btn.click()

time.sleep(1)

no1_btn = driver.find_element(By.CLASS_NAME, 'context_external_tool_18')
no1_btn.click()
time.sleep(8)



time.sleep(15)
