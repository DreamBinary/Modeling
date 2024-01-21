import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service  # 新增
from selenium.webdriver.common.by import By

max_size = 0
path = "D:\MyPython\msedgedriver.exe"
service = Service(executable_path=path)
for  i in range(0, max_size):
    driver = webdriver.Edge(service=service)

    driver.get("https://dict.youdao.com/result?word=english&lang=en")
    time.sleep(5)
    button = driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div/div/div/div[1]/div/div/section/div[2]/div[1]/div/ul/li[2]")
    print(button)
    button.click()
    selenium_page = driver.page_source
    print(selenium_page)
    driver.quit()
    time.sleep(2)
