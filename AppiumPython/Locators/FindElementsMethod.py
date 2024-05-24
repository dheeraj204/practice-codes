from appium import webdriver
import time
from selenium.webdriver.common.by import By

desired_caps = {}
desired_caps["platformName"] = "Android"
desired_caps["platformVersion"] = "10"
desired_caps["deviceName"] = "Pixel3XL"
desired_caps["app"] = "D:\Codes\AppiumPython\Android_Demo_App.apk"
desired_caps["appPackage"] = "com.**"
desired_caps["appActivity"] = "com.**.MainActivity"

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

element = driver.find_elements(By.CLASS_NAME, "android.widget.Button")

for x in element:
    print(x.text)

for x in element:
    button = x.text
    if button == "ScrollView":
        x.click()
        break


time.sleep(5)
driver.quit()
