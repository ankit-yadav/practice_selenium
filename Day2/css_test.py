from selenium import webdriver
from selenium.webdriver.common.by import By
##1 way to get the chrome driver obj
from selenium.webdriver.chrome.service import Service
serv_obj = Service("C:\drivers\chromdriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj) #this opens the browser

driver.get("https://magento.softwaretestingboard.com/customer/account/login/referer/aHR0cHM6Ly9tYWdlbnRvLnNvZnR3YXJldGVzdGluZ2JvYXJkLmNvbS8%2C/")

###   CSS :-tag and id
#driver.find_element(By.CSS_SELECTOR, "input#email").send_keys("yadavankit2211@gmail.com")
driver.find_element(By.CSS_SELECTOR, "#email").send_keys("yadavankit2211@gmail.com")

###   CSS :-tag and class and attribute
driver.find_element(By.CSS_SELECTOR, "input.input-text[title=Password]").send_keys("Global@123")
#driver.find_element(By.CSS_SELECTOR, "input-text[class=input-text]").send_keys("Global@123")


driver.find_element(By.ID, "send2").click()

driver.implicitly_wait(20)
###   CSS :-tag and attribute
driver.find_element(By.CSS_SELECTOR, "img[alt=Hero Hoodie]").click()

