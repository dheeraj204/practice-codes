from selenium.common import NoSuchElementException

from .base_activity import BaseActivity
from .base import Button, AppiumBy
from appium.webdriver import Remote
from .home import Home
from .simpl import SimplePage


class PaymentsPage(BaseActivity):
    ACITIVITY = ".MainActivity"

    def __init__(self, driver: Remote):
        super().__init__(driver)
        self.driver = driver
        self.loc = "afknsdjf"
        self.home_page = Home(self.driver)
        self.simpl = SimplePage(self.driver)

    def launch(self):
        if not self.loaded:
            self.simpl.launch()
            if not self.simpl.paynow_button.is_visible():
                self.scroll_to_top()
            self.simpl.paynow_button.click()

    @property
    def loaded(self):
        self.wait_time(timeout=2)
        loc = (AppiumBy.XPATH, "//android.widget.TextView[@text='Pay to Simpl']")
        try:
            return self.driver.find_element(*loc).is_displayed()
        except NoSuchElementException:
            return False

    @property
    def payment_amount(self):
        loc = (
            AppiumBy.XPATH,
            "//android.widget.TextView[@text='Paying']//following-sibling::android.widget.TextView",
        )
        return float(self.driver.find_element(*loc).text.strip("₹"))

    @property
    def payment_options(self):
        loc = (AppiumBy.XPATH, "//android.widget.Button[@text='OTHER PAYMENT OPTIONS']")
        return Button(driver=self.driver, locator=loc)

    def open_payment_options(self):
        if not self.card_payment_options.is_visible():
            self.payment_options.click()
            self.swipe(direction="up", distance=600)

    @property
    def card_payment_options(self):
        loc = (AppiumBy.XPATH, "//android.widget.Button[@text='Card Payment']")
        return Button(driver=self.driver, locator=loc)

    def open_card_payment(self):
        if not self.card_payment_options.is_visible():
            self.open_payment_options()
            self.card_payment_options.click()
            self.swipe(direction="up", distance=600)

    @property
    def card_details_buttton(self):
        loc = (
            AppiumBy.XPATH,
            "//android.widget.TextView[@text='Enter your card details']",
        )
        return Button(driver=self.driver, locator=loc)

    def open_card_details(self):
        self.open_card_payment()
        self.card_details_buttton.click()
        self.swipe(direction="up", distance=600)

    @property
    def payment_button(self):
        loc = (AppiumBy.XPATH, "//android.widget.Button[contains(@text, 'PAY ₹')]")
        return Button(driver=self.driver, locator=loc)

    @property
    def card_details_error(self):
        loc = (
            AppiumBy.XPATH,
            "//android.widget.TextView[@text='Enter correct card details.']",
        )
        return self.driver.find_element(*loc)
