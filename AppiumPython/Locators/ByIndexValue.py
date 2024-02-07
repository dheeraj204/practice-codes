from selenium.webdriver.common.by import By
from appium import webdriver


desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '10'
desired_caps['deviceName'] = 'Pixel3XL'
desired_caps['app'] = "D:\Codes\AppiumPython\Android_Demo_App.apk"
desired_caps['appPackage'] = 'com.**'
desired_caps['appActivity'] = 'com.**MainActivity'

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

# ele_index = driver.find_element_by_android_uiautomator('UiSelector().description("Btn3")')
# ele_index.click()
driver.find_element(By.ID, '//android.widget.Button[@content-desc="Btn3"]').click()
