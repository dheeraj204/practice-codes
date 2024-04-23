from time import sleep
from appium.webdriver import Remote, WebElement
from appium.webdriver.common.appiumby import AppiumBy

from selenium.common.exceptions import NoSuchElementException, WebDriverException
from appium.webdriver.common.touch_action import TouchAction


class Button:

    def __init__(self, driver: Remote, locator: tuple[str, str]):
        self.driver = driver
        self.locator = locator

    def is_displayed(self) -> bool:
        try:
            return self.wait_visible().is_displayed()
        except NoSuchElementException:
            return False

    def is_visible(self) -> bool:
        try:
            self.driver.find_element(*self.locator).is_displayed()
            return True
        except NoSuchElementException:
            return False

    def is_selected(self) -> bool:
        try:
            return self.driver.find_element(*self.locator).is_selected()
        except NoSuchElementException:
            return False

    def wait_visible(self, timeout=5) -> WebElement:
        i = 0
        while i != timeout:
            if self.is_visible():
                return self.driver.find_element(*self.locator)
            else:
                sleep(0.5)
                i += 1
        raise NoSuchElementException(
            "Element never became visible: %s (%s)" % (self.locator[0], self.locator[1])
        )

    def wait_for_text(self, text, timeout=10):
        i = 0
        while i != timeout:
            try:
                element = self.driver.find_element(*self.locator)
                element_text = element.text
                if element_text.lower() == text.lower():
                    return True
                else:
                    pass
            except NoSuchElementException:
                pass
            sleep(1)
            i += 1
        raise Exception(
            "Element text never became visible: %s (%s) - %s"
            % (self.locator[0], self.locator[1], text)
        )

    def click(self) -> None:
        element = self.wait_visible()
        element.click()

    def send_keys(self, text) -> None:
        element = self.wait_visible(timeout=2)
        element.send_keys(text)

    def scroll_up(self):
        loc = (AppiumBy.XPATH, "//android.widget.TextView")
        elements = self.driver.find_elements(*loc)
        self.driver.scroll(elements[-1], elements[1])

    def scroll_to_element(self, timeout=5):
        i = 0
        while i != timeout:
            if self.is_visible():
                return
            else:
                self.swipe(direction="up", distance=700)
                i += 1
        while i != timeout:
            if self.is_visible():
                return
            else:
                self.swipe(direction="down", distance=700)
                i += 1

    def get_to_element(self, retries=5) -> bool:
        i = 0
        while i != retries:
            if self.is_visible():
                return self.is_visible()
            else:
                sleep(0.5)
                self.swipe("down")
                i += 1
            if self.is_visible():
                return self.is_visible()
            else:
                sleep(0.5)
                self.swipe("down")
                i += 1
        raise Exception(
            "Element never became visible: %s (%s)" % (self.locator[0], self.locator[1])
        )

    def long_press(self, duration=1000) -> None:
        element = self.driver.find_element(*self.locator)
        action = TouchAction(self.driver)
        action.long_press(element, None, None, duration).perform()

    def swipe(self, direction="up", shift=350, distance=500):
        """
        Swipe up, down, left, or right on the activity
        """
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

    def hide_keyboard(self) -> None:
        try:
            sleep(1)
            self.driver.hide_keyboard()
        except WebDriverException:
            pass
