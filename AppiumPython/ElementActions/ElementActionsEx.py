import time
from selenium.webdriver.common.by import By
from appium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '10'
desired_caps['deviceName'] = 'Pixel_4_API_29'
desired_caps['app'] = "D:\Codes\AppiumPython\Android_Demo_App.apk"
desired_caps['appPackage'] = 'com.**'
desired_caps['appActivity'] = 'com.**.MainActivity'

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

ele_id = driver.find_element(By.ID, "")
print("Text on the button :", ele_id.text)
print("Text on the button :", ele_id.get_attribute("name"))
ele_id.click()

ele_className = driver.find_element(By.CLASS_NAME, "android.widget.EditText")
ele_className.send_keys("sample")
time.sleep(2)
ele_className.clear()
