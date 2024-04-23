from .base_activity import BaseActivity
from .base import Button, AppiumBy
from .login_page import LoginPage
from appium.webdriver import Remote
import subprocess


class Home(BaseActivity):
    ACITIVITY = ".MainActivity"

    def __init__(self, driver: Remote):
        super().__init__(driver)
        self.driver = driver
        self.login_page = LoginPage(driver=self.driver)

    def launch(self):
        if not self.loaded:
            self.driver.back()
            subprocess.run(
                "adb shell am start -n com.simpl.android/com.simpl.android.MainActivity"
            )
            if not self.simpl_page.is_displayed():
                if self.login_page.loaded:
                    self.login_page.perform_login(number="")  # mobile number
            self.check_and_close()

    def open_app(self):
        self.driver.activate_app("com.simpl.android")

    @property
    def loaded(self):
        return self.current_activity == self.ACITIVITY and self.simpl_page.is_visible()

    @property
    def simpl_page(self):
        locator = (AppiumBy.ACCESSIBILITY_ID, "Home")
        return Button(driver=self.driver, locator=locator)

    @property
    def shop_page(self):
        locator = (AppiumBy.ACCESSIBILITY_ID, "shopstack")
        return Button(driver=self.driver, locator=locator)

    @property
    def transactions_page(self):
        locator = (AppiumBy.ACCESSIBILITY_ID, "transactions")
        return Button(driver=self.driver, locator=locator)

    @property
    def billbox_page(self):
        locator = (AppiumBy.ACCESSIBILITY_ID, "billbox")
        return Button(driver=self.driver, locator=locator)

    @property
    def more_page(self):
        locator = (AppiumBy.ACCESSIBILITY_ID, "morestack")
        return Button(driver=self.driver, locator=locator)
