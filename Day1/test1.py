#############################
# Login the web page
# Input login credentials and verify the actual and expected titile of the page
#############################

from selenium import webdriver
from selenium.webdriver.common.by import By
##1 way to get the chrome driver obj
from selenium.webdriver.chrome.service import Service
serv_obj = Service("C:\drivers\chromdriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj) #this opens the browser
#"C:\drivers\chromdriver_win32\chromedriver.exe

#2nd way to get the chrome driver
#driver = webdriver.Chrome()
#get opens the url
driver.get("https://magento.softwaretestingboard.com/customer/account/login/referer/aHR0cHM6Ly9tYWdlbnRvLnNvZnR3YXJldGVzdGluZ2JvYXJkLmNvbS9jdXN0b21lci9hY2NvdW50L2xvZ291dFN1Y2Nlc3Mv/")
##now find the element and input the username
driver.find_element(By.ID,value="email").send_keys("yadavankit2211@gmail.com")
driver.find_element(by=By.NAME,value="login[password]").send_keys("Global@123")
driver.find_element(By.ID,value="send2").click()
print(driver.title)
#driver.close()