from appium import webdriver
import time
from selenium.webdriver.common.by import By

# https://stackoverflow.com/questions/7789826/adb-shell-input-events

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '10'
desired_caps['deviceName'] = 'Pixel_4_API_29'
desired_caps['app'] = "D:\Codes\AppiumPython\Android_Demo_App.apk"
desired_caps['appPackage'] = 'com.**'
desired_caps['appActivity'] = 'com.**.MainActivity'

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

ele_id = driver.find_element(By.ID, "com.**:id/EnterValue")
ele_id.click()

ele_className = driver.find_element(By.CLASS_NAME, "android.widget.EditText")
ele_className.send_keys("sample")
ele_className.click()
time.sleep(2)
driver.press_keycode(67)
driver.press_keycode(67)
time.sleep(2)
driver.press_keycode(4)
driver.press_keycode(4)
