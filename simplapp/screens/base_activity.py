import time
from .base import Button
from appium.webdriver import Remote
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException, WebDriverException


class BaseActivity:
    ACITIVITY = ".MainActivity"

    def __init__(self, driver: Remote):
        self.driver = driver

    @property
    def current_activity(self):
        return self.driver.current_activity

    def open_app(self):
        self.driver.activate_app("com.simpl.android")

    @property
    def auto_pay_popup(self):
        loc = (
            AppiumBy.XPATH,
            "//android.widget.TextView[@text='DO NOT REMIND ME AGAIN']",
        )
        return Button(driver=self.driver, locator=loc)

    def check_and_close(self):
        try:
            if self.auto_pay_popup.is_displayed():
                self.auto_pay_popup.click()
        except NoSuchElementException:
            pass

    def wait_time(self, timeout=3):
        time.sleep(timeout)

    def swipe(self, direction="up", shift=350, distance=500):
        dirs = ["up", "down", "left", "right"]
        if direction.lower() not in dirs:
            raise ValueError(f"Direction can only be {dirs}")
        x, y = self.driver.get_window_size().values()
        x = int(x / 2)
        y = y - shift
        if direction.lower() == "up":
            coords = (x, y, x, y - shift)
        elif direction.lower() == "down":
            y = y - shift
            coords = (x, y, x, y + shift)
        elif direction.lower() == "right":
            coords = (x, y, x - shift, y)
        else:
            x = x - shift
            coords = (x, y, x + shift, y)
        for _ in range(int(distance / shift)):
            self.driver.swipe(*coords)

    def scroll_to_top(self):
        for _ in range(5):
            self.swipe(direction="down", distance=700)

    def scroll_to_bottom(self):
        for _ in range(5):
            self.swipe(direction="up", distance=700)
