from appium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '10'
desired_caps['deviceName'] = 'Pixel_4_API_29'
desired_caps['app'] = "D:\Codes\AppiumPython\Android_Demo_App.apk"
desired_caps['appPackage'] = 'com.**'
desired_caps['appActivity'] = 'com.**.MainActivity'

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

#ele_text = driver.find_element_by_android_uiautomator('new UiSelector().text("ENTER SOME VALUE")')
ele_text = driver.find_element_by_android_uiautomator('text("ENTER SOME VALUE")')
ele_text.click()