from appium.webdriver.common.appiumby import AppiumBy

from .home import BaseActivity, Remote, Home, Button


class SimplePage(BaseActivity):
    def __init__(self, driver: Remote):
        super().__init__(driver)
        self.home = Home(driver=driver)

    def launch(self):
        if not self.loaded:
            self.home.launch()
            self.home.simpl_page.click()

    @property
    def loaded(self):
        return (
            self.current_activity == self.ACITIVITY
            and self.home.simpl_page.is_selected()
        )

    @property
    def paynow_button(self):
        locator = (AppiumBy.XPATH, "//android.widget.TextView[@text='Pay Now']")
        return Button(driver=self.driver, locator=locator)

    @property
    def available_limit(self):
        locator = (
            AppiumBy.XPATH,
            "//android.widget.TextView[@text='Available limit']//following-sibling::android.widget.TextView",
        )
        return self.driver.find_element(*locator).text.strip("₹").replace(",", "")

    @property
    def simpl_bill_amount(self):
        locator = (
            AppiumBy.XPATH,
            "//android.widget.TextView[@text='Your Simpl bill']//following-sibling::android.widget.TextView",
        )
        return self.driver.find_element(*locator).text.strip("₹").replace(",", "")

    def profile_verification(self):
        locator = (
            AppiumBy.XPATH,
            "//android.widget.TextView[@text='Verify your Simpl profile']",
        )
        return Button(driver=self.driver, locator=locator)

    @property
    def user_name(self):
        locator = (
            AppiumBy.XPATH,
            "//android.widget.TextView[@text='Hi ']//following-sibling::android.widget.TextView",
        )
        return self.driver.find_element(*locator)

    def navigate_to_offers_by_category(self):
        locator = (
            AppiumBy.XPATH,
            "//android.widget.TextView[@text='Offers by Category']",
        )
        return Button(driver=self.driver, locator=locator).scroll_to_element()

    @property
    def explore_button(self):
        locator = (AppiumBy.ACCESSIBILITY_ID, "Explore")
        return Button(driver=self.driver, locator=locator)

    def navigate_to_partner_brands(self) -> None:
        locator = (
            AppiumBy.XPATH,
            "//android.widget.TextView[@text='Partner brands']",
        )
        Button(driver=self.driver, locator=locator).scroll_to_element()

    @property
    def partner_brands_button(self) -> Button:
        locator = (
            AppiumBy.XPATH,
            '(//android.view.ViewGroup[@content-desc="View All"])[2]',
        )
        return Button(driver=self.driver, locator=locator)

    def partner_brands(self) -> list:
        locator = (AppiumBy.CLASS_NAME, "android.widget.TextView")
        brands_obj = self.driver.find_elements(*locator)
        brands = []
        for i in brands_obj:
            brands.append(i.text)
        return brands
