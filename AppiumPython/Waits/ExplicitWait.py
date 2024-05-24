from appium import webdriver
import time

from selenium.common.exceptions import (
    ElementNotVisibleException,
    ElementNotSelectableException,
    NoSuchElementException,
)
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

desired_caps = {}
desired_caps["platformName"] = "Android"
desired_caps["platformVersion"] = "10"
desired_caps["deviceName"] = "Pixel3XL"
desired_caps["app"] = "D:\Codes\AppiumPython\Android_Demo_App.apk"
desired_caps["appPackage"] = "com.**"
desired_caps["appActivity"] = "com.**.MainActivity"

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

wait = WebDriverWait(
    driver,
    25,
    poll_frequency=1,
    ignored_exceptions=[
        ElementNotVisibleException,
        ElementNotSelectableException,
        NoSuchElementException,
    ],
)

# ele = wait.until(lambda  x: x.find_element_by_id("com.**:id/EnterValue"))
# ele.click()

# ele = wait.until(lambda  x: x.find_element_by_class_name("android.widget.EditText")).send_keys("Code2Lead")
# ele = wait.until(lambda  x: x.find_element_by_android_uiautomator('UiSelector().description("Btn3")'))
ele = wait.until(
    lambda x: x.find_element_by_android_uiautomator('text("ENTER SOME VALUE")')
)
ele.click()

time.sleep(4000)
driver.quit()
