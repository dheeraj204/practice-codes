from appium import webdriver

desired_caps = {'platformName': 'Android', 'platformVersion': '10', 'deviceName': 'Pixel_4_API_29',
                'app': "D:\Codes\AppiumPython\Android_Demo_App.apk", 'appPackage': 'com.88',
                'appActivity': 'com.***.MainActivity'}

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

ele_id = driver.find_element("")
ele_id.click()
