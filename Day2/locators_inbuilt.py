
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_exe=Service("C:\drivers\chromdriver_win32\chromedriver.exe")
driver= webdriver.Chrome(service=chrome_exe)


driver.get("https://magento.softwaretestingboard.com/")

#to maxmize  & minimize the window
driver.maximize_window()
driver.minimize_window()

#driver.find_element(By.LINK_TEXT, "What's New").click()
driver.find_element(By.PARTIAL_LINK_TEXT, 'New').click()

##return all the link available in the opened web page
list_links = driver.find_elements(by=By.TAG_NAME, value="a")
print(list_links)


#driver.close()