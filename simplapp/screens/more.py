from appium.webdriver.common.appiumby import AppiumBy

from .home import BaseActivity, Remote, Home, Button


class MorePage(BaseActivity):
    def __init__(self, driver: Remote):
        super().__init__(driver)
        self.home = Home(driver=driver)

    def launch(self):
        if not self.loaded:
            self.home.launch()
            self.home.more_page.click()

    @property
    def loaded(self):
        return self.home.loaded and self.home.more_page.is_selected()

    @property
    def refer_button(self):
        locator = (AppiumBy.XPATH, "//android.widget.TextView[@text='Refer & Earn']")
        return Button(driver=self.driver, locator=locator)

    @property
    def profile_button(self):
        locator = (AppiumBy.XPATH, "//android.widget.TextView[@text='Profile']")
        return Button(driver=self.driver, locator=locator)

    @property
    def merchants_support_button(self):
        locator = (
            AppiumBy.XPATH,
            "//android.widget.TextView[@text='Merchants we support']",
        )
        return Button(driver=self.driver, locator=locator)

    @property
    def my_merchants_button(self):
        locator = (AppiumBy.XPATH, "//android.widget.TextView[@text='My Merchants']")
        return Button(driver=self.driver, locator=locator)

    @property
    def help_centre_button(self):
        locator = (AppiumBy.XPATH, "//android.widget.TextView[@text='Help Centre']")
        return Button(driver=self.driver, locator=locator)

    @property
    def privacy_policy_button(self):
        locator = (AppiumBy.XPATH, "//android.widget.TextView[@text='Privacy Policy']")
        return Button(driver=self.driver, locator=locator)

    @property
    def signout_button(self):
        locator = (AppiumBy.XPATH, "//android.widget.TextView[@text='Sign out']")
        return Button(driver=self.driver, locator=locator)

    @property
    def signout_no_button(self):
        locator = (AppiumBy.XPATH, "//android.widget.TextView[@text='NO, STAY']")
        return Button(driver=self.driver, locator=locator)

    @property
    def signout_yes_button(self):
        locator = (AppiumBy.XPATH, "//android.widget.TextView[@text='YES, SURE']")
        return Button(driver=self.driver, locator=locator)
