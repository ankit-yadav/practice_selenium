from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

serv_ob = Service("C:\drivers\chromdriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_ob)
driver.maximize_window()
driver.get("https://magento.softwaretestingboard.com/")
driver.find_element(By.XPATH, "//*[@id='ui-id-7']/span[1]").click()