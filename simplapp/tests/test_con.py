import time
from selenium.common.exceptions import NoSuchElementException
from screens import (
    Home,
    PaymentsPage,
    LoginPage,
    SimplePage,
    MorePage,
    TransactionsPage,
)


class TestingHome:

    def test_launch(self, appium_driver):
        self.home_Act = Home(appium_driver)
        self.simpl = SimplePage(appium_driver)
        self.home_Act.open_app()
        if not self.home_Act.loaded:
            raise AssertionError("home page was not loaded")

    def test_verify_partner_brands(self, appium_driver):
        expected_brands = [
            "bbInstant",
            "FirstCry",
            "Rapido",
            "JioMart",
            "Myntra",
            "MakeMyTrip",
            "Meesho",
            "redBus",
            "magicpin",
            "Nykaa",
            "Apollo Pharmacy",
            "MyJio",
            "bigbasket",
            "blinkit",
            "Zepto",
        ]
        self.simpl = SimplePage(appium_driver)
        self.simpl.launch()
        self.simpl.navigate_to_partner_brands()
        try:
            self.simpl.partner_brands_button.click()
            self.simpl.wait_time(1)
            assert set(expected_brands).issubset(set(self.simpl.partner_brands()))
        finally:
            appium_driver.back()
            self.simpl.scroll_to_top()

    def test_username(self, appium_driver):
        self.home_Act = Home(appium_driver)
        self.simpl = SimplePage(appium_driver)
        self.home_Act.launch()
        if not self.home_Act.loaded:
            raise AssertionError("home page was not loaded")
        self.simpl.launch()
        try:
            _ = self.simpl.user_name.text
        except NoSuchElementException:
            self.home_Act.scroll_to_top()
        assert self.simpl.user_name.text == "dheeraj"

    def test_simpl_bill(self, appium_driver):
        self.simpl = SimplePage(appium_driver)
        self.transactions = TransactionsPage(appium_driver)
        self.simpl.launch()
        self.simpl.scroll_to_top()
        try:
            current_bill = float(self.simpl.simpl_bill_amount)
        except NoSuchElementException:
            self.simpl.scroll_to_top()
            current_bill = float(self.simpl.simpl_bill_amount)
        self.transactions.launch()
        time.sleep(1)
        while True:
            self.transactions.this_month_button.click()
            if self.transactions.fileter_selected:
                break
        time.sleep(1)
        pending_amount = self.transactions.total_transactions()["pending_amount"]
        assert current_bill == pending_amount

    def test_login(self, appium_driver):
        self.loginpage = LoginPage(appium_driver)
        if self.loginpage.loaded:
            self.loginpage.login_field.send_keys("")  # mobile number
            assert self.loginpage.login_field.text == ""  # mobile number
            assert self.loginpage.continue_button.is_displayed()

    def test_logout_and_login(self, appium_driver):
        self.loginpage = LoginPage(appium_driver)
        self.more_page = MorePage(appium_driver)
        self.home_Act = Home(appium_driver)
        self.home_Act.launch()
        self.more_page.launch()
        assert self.more_page.loaded
        self.more_page.signout_button.click()
        assert self.more_page.signout_yes_button.is_displayed()
        self.more_page.signout_yes_button.click()
        assert self.loginpage.loaded
        self.loginpage.perform_login("7995311865")

    def test_billbox_popuphandle(self, appium_driver):
        self.home_Act = Home(appium_driver)
        self.home_Act.billbox_page.click()
        self.home_Act.check_and_close()

    def test_payment_options(self, appium_driver):
        self.payments = PaymentsPage(appium_driver)
        try:
            self.payments.launch()
            assert self.payments.loaded
            self.payments.open_card_payment()
        finally:
            appium_driver.back()

    def test_invalid_payment_details(self, appium_driver):
        self.payments = PaymentsPage(appium_driver)
        try:
            self.payments.launch()
            assert self.payments.loaded
            self.payments.open_card_payment()
            self.payments.open_card_details()
            self.payments.payment_button.click()
            assert self.payments.card_details_error.is_displayed()
        finally:
            appium_driver.back()

    def test_verify_final_payment_amount(self, appium_driver):
        self.payments = PaymentsPage(appium_driver)
        self.simpl = SimplePage(appium_driver)
        self.simpl.launch()
        try:
            current_bill = float(self.simpl.simpl_bill_amount)
        except NoSuchElementException:
            self.simpl.scroll_to_top()
            current_bill = float(self.simpl.simpl_bill_amount)
        try:
            self.simpl.paynow_button.click()
            assert self.payments.loaded
            final_amount = self.payments.payment_amount
            assert current_bill == final_amount
        finally:
            appium_driver.back()
