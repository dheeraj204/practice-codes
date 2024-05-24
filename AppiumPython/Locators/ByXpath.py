import time
from selenium.webdriver.common.by import By
from appium import webdriver

desired_caps = {}
desired_caps["platformName"] = "Android"
desired_caps["platformVersion"] = "10"
desired_caps["deviceName"] = "Pixel3XL"
desired_caps["app"] = "D:\Codes\AppiumPython\Android_Demo_App.apk"
desired_caps["appPackage"] = "com.**"
desired_caps["appActivity"] = "com.**.MainActivity"

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

# ele_xpath = find_element(By.XPATH,'//android.widget.Button[@content-desc="Btn1"]') - Using Xpath_and Content-Des
# ele_xpath = find_element(By.XPATH,'//android.widget.Button[@resource-id="com.**:id/EnterValue"]')  -
# Using Xpath_and id ele_xpath = find_element(By.XPATH,'//android.widget.Button[2]')  - Using Xpath_and index
# ele_xpath = find_element(By.XPATH,'//android.widget.Button[@text="ScrollView"]')  - Using Xpath_and text
ele_xpath = driver.find_element(
    By.XPATH, '//android.widget.Button[@resource-id="com.**:id/EnterValue"]'
)
ele_xpath.click()

driver.find_element(By.XPATH, "//android.widget.EditText").send_keys(
    "sample"
)  # - Using Xpath_and className

time.sleep(2000)

driver.quit()
