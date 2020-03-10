import platform
import time
from selenium import webdriver

user = 'rechnungen@fine-wall-berlin.de'
pw = 'HPPageWideProMFP477dw'


options = webdriver.ChromeOptions()
options.add_argument('headless')
driver_path = r'C:\ProgramData\chocolatey\lib\chromedriver\tools\chromedriver.exe'

browser = webdriver.Chrome(options=options, executable_path=driver_path)
browser.set_window_size(1366, 768)
browser.get("https://kundenbereich.financial-service-plus.de/")
browser.find_element_by_id("UserNameTb_I").send_keys(user)
browser.find_element_by_id("UserPasswordTb_I").send_keys(pw)

browser.find_element_by_id("BtnLogin_CD").click()

time.sleep(5)

html = browser.page_source

if 'Arndt' in html:
    print("logged in :)")
else:
    print('login failed :/')

