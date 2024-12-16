#20232071 조준용
#lms에 접속하여 자동으로 로그인 후, lms의 달력창에 들어가서 해당 월에 등록되어 있는 과제 등의 일정을
#바탕화면에 "12월 일정" 이라는 txt 파일을 만들어 저장하여 오프라인 상황에서도 과제 정보를 볼 수 있는 코드이다.

#코드 실행에 필요한 모듈 및 패키지 import
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#셀레니움을 통해 chrome창을 열 때 사용할 옵션들, 열리는 창의 크기 설정 및 창의 자동으로 닫힘 방지
options = Options()
options.add_argument("--start-maximized")
options.add_experimental_option("detach", True)

#lms.hanbat 웹 오픈 -> 로그인 창으로 들어간다
driver = webdriver.Chrome(options=options)
driver.get('https://lms.hanbat.ac.kr/')

#창이 열리기까지 시간이 조금 걸리므로 2초 기다려서 안정성을 높인다. 이후 time.sleep도 동일
time.sleep(2)

#Id 입력하는 칸의 ID인 login_user_id 를 찾고, 사용자의 id(학번)을 입력해준다
id_btn = driver.find_element(By.ID, 'login_user_id')
id_btn.send_keys('20232071')

#pw 입력하는 칸의 ID인 login_user_password 를 찾고, 사용자의 pw(비밀번호)을 입력해준다
pw_btn = driver.find_element(By.ID, 'login_user_password')
#이때, 비밀번호 입력 칸은 활성화 되어 있지 않으므로 한번 클릭 후 입력하게 한다
pw_btn.click()
pw_btn.send_keys('cho182931!')

#id와 비밀번호를 모두 입력하여 로그인 버튼을 찾고 누르기.
login_btn = driver.find_element(By.CLASS_NAME, 'login_btn')
login_btn.click()
time.sleep(1)

#lms의 calender 버튼을 찾고 눌러준다
calen_btn = driver.find_element(By.ID, 'global_nav_calendar_link')
calen_btn.click()
time.sleep(1)

#오늘이 몇 월 인지 확인한다
now = datetime.now()
month = now.month

#위에서 설정한 월 변수를 이용하여 파일 위치(바탕화면) 및 파일 이름과, txt파일의 제일 위에 입력 될 헤더를 설정한다
file_name = f"C:/Users/junyo/OneDrive/바탕 화면/{month}월 일정.txt"
file_header = f"{month}월의 과제 및 일정 입니다.\n\n"

#w모드 (쓰기 모드) 로 전에 설정한 경로 및 이름으로 파일을 열어서 헤더를 위에 작성.
f = open(file_name, "w")
f.write(file_header)

#lms의 캘린더에 등록 되어 있는 일정의 class name을 이용하여 schedule에 저장.(모든 일정을 긁어 모은다)(텍스트 추출)
schedule = driver.find_elements(By.CLASS_NAME, "fc-event-container")

#j 초기값 1 설정 (몇번째 인지 나타내는 번호를 의미 하는 j 변수)
j = 1

#반복문 실행. 보기 좋게 12월 일정.txt 파일에 저장이 되며 동시에 console(cmd) 창에도 print 된다.
for i in schedule:
    f.write(str(j) + ". -------------------------\n")
    title = i.text
    print(title+"\n")
    f.write(title)
    f.write("\n----------------------------\n\n\n")
    j = j + 1

#open 한 파일 닫기
f.close()

#파일이 안정적으로 저장 될 15초 정도를 기다린 후 웹 닫기.
time.sleep(15)
driver.quit()