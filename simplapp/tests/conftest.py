import subprocess

import pytest
from appium.webdriver import Remote
from appium.options.android import UiAutomator2Options
from appium.webdriver.appium_service import AppiumService
from screens.base import Button
import logging


def desired_capabilities():
    options = UiAutomator2Options()
    desired_caps = {
        "platformName": "Android",
        "udid": "",
        "automationName": "uiautomator2",
        "enableMultiWindows": True,
        "noReset": True,
        "unlockType": "pin",  # password, pattern
        "unlockKey": "",  # password or number assigned for pattern
    }
    for name, value in desired_caps.items():
        options.set_capability(name=name, value=value)
    return options


@pytest.fixture(scope="session")
def appium_driver():
    AppiumService().start()
    driver_obj = Remote("http://127.0.0.1:4723", options=desired_capabilities())
    driver_obj.implicitly_wait(time_to_wait=10)
    yield driver_obj
    print("stop")
    subprocess.call("taskkill /F /IM node.exe")
    AppiumService().stop()


# @pytest.fixture()
# def screens(appium_driver):
#     yield Button(appium_driver)
