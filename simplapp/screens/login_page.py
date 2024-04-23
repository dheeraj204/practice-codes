from .base_activity import BaseActivity
from .base import Button, AppiumBy
from appium.webdriver import Remote


class LoginPage(BaseActivity):
    ACITIVITY = ".MainActivity"

    def __init__(self, driver: Remote):
        super().__init__(driver)
        self.driver = driver

    def launch(self):
        pass

    @property
    def loaded(self):
        locator = (
            AppiumBy.XPATH,
            "//android.widget.TextView[@text='Simpl will verify this number']",
        )
        return Button(driver=self.driver, locator=locator).is_displayed()

    @property
    def login_field(self):
        locator = (
            AppiumBy.XPATH,
            "//android.widget.EditText[@content-desc='MobileNumber']",
        )
        return self.driver.find_element(*locator)

    @property
    def continue_button(self):
        locator = (AppiumBy.ACCESSIBILITY_ID, "commonButton")
        return Button(driver=self.driver, locator=locator)

    @property
    def allow_button(self):
        locator = (AppiumBy.ID, "com.google.android.gms:id/positive_button")
        return Button(driver=self.driver, locator=locator)

    def perform_login(self, number: str):
        if self.loaded:
            self.login_field.send_keys(number)
            self.wait_time()
            self.continue_button.click()
            self.allow_button.wait_visible(timeout=15)
            self.allow_button.click()
            self.wait_time()
