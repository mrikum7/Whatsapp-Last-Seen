import time
from selenium import webdriver

switch = 0

firefox = webdriver.Firefox()
firefox.get('http://web.whatsapp.com')

time.sleep(10)

while True:
    t = time.localtime()
    try:
        ele = firefox.find_element_by_css_selector('._3-cMa')
        if switch == 0 and ele.text == 'online':
            print(f'{t.tm_hour}:{t.tm_min}:{t.tm_sec} ONLINE')
            switch = 1
    except:
        if switch == 1:
            print(f'{t.tm_hour}:{t.tm_min}:{t.tm_sec} OFFLINE')
            switch = 0
    time.sleep(1)

