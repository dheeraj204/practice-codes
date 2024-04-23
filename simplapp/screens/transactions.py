from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import NoSuchElementException

from .home import BaseActivity, Remote, Home, Button


class TransactionsPage(BaseActivity):
    def __init__(self, driver: Remote):
        super().__init__(driver)
        self.home = Home(driver=driver)

    def launch(self):
        if not self.loaded:
            self.home.launch()
            self.home.transactions_page.click()

    @property
    def loaded(self):
        return self.home.loaded and self.this_month_button.is_visible()

    @property
    def this_month_button(self):
        locator = (AppiumBy.XPATH, "//android.widget.TextView[@text='This month']")
        return Button(driver=self.driver, locator=locator)

    @property
    def last_month_button(self):
        locator = (AppiumBy.XPATH, "//android.widget.TextView[@text='Last month']")
        return Button(driver=self.driver, locator=locator)

    @property
    def filter_button(self):
        locator = (AppiumBy.XPATH, "//android.widget.TextView[@text='Filter']")
        return Button(driver=self.driver, locator=locator)

    @property
    def fileter_selected(self):
        loc = (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="1, , Filter"]')
        try:
            return self.driver.find_element(*loc).is_displayed()
        except NoSuchElementException:
            return False

    def total_transactions(self):
        locator = (
            AppiumBy.XPATH,
            '//android.widget.TextView[@content-desc="transaction-item-amount"]',
        )
        failed_locator = (
            AppiumBy.XPATH,
            "//android.widget.TextView[@content-desc='transaction-item-status']/parent::android.view.ViewGroup",
        )
        failed_amount = float(
            self.driver.find_element(*failed_locator)
            .find_element(*locator)
            .text.strip("₹")
        )
        locs = self.driver.find_elements(*locator)
        self.swipe(direction="up", distance=600)
        locs2 = self.driver.find_elements(*locator)
        locs.extend(locs2)
        final_elements = list(set(locs))
        amount_paid = 0
        pending_amount = 0
        for amnt in final_elements:
            # if
            if amnt.text.startswith("+"):
                amount_paid += float(amnt.text.strip("+ ₹"))
            else:
                pending_amount += float(amnt.text.strip("+ ₹"))
        return {
            "amount_paid": amount_paid,
            "pending_amount": pending_amount - failed_amount,
        }

    def filter_page_loaded(self):
        locator = (AppiumBy.XPATH, '//android.widget.TextView[@text="Time Period"]')
        return self.driver.find_element(*locator).is_displayed()
