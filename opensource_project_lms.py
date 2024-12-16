from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get('https://lms.hanbat.ac.kr/')

time.sleep(2)

id_box = driver.find_element(By.ID, 'login_user_id')
id_box.send_keys('20232071')

pw_box = driver.find_element(By.ID, 'login_user_password')
pw_box.click()
time.sleep(1)
pw_box.send_keys('cho182931!')

time.sleep(1)
login_btn = driver.find_element(By.CLASS_NAME, 'login_btn')
login_btn.click()

time.sleep(5)

firstclass_btn = driver.find_element(By.CLASS_NAME, 'ic-DashboardCard')
firstclass_btn.click()

time.sleep(10)

