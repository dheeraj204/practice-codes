from appium import webdriver
from selenium.webdriver.common.by import By

desired_caps = {}
desired_caps["platformName"] = "Android"
desired_caps["platformVersion"] = "10"
desired_caps["deviceName"] = "Pixel_4_API_29"
desired_caps["app"] = "D:\Codes\AppiumPython\Android_Demo_App.apk"
desired_caps["appPackage"] = "com.**"
desired_caps["appActivity"] = "com.**.MainActivity"

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

element_by_id = driver.find_element(By.ID, "com.**:id/EnterValue")

print("Current Activity", driver.current_activity)
print("Current context", driver.current_context)
print("Current orientation", driver.orientation)
print("Check Whether device is locked or not :", driver.is_locked())
