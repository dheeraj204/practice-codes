from .home import BaseActivity, Remote, Home


class ShopPage(BaseActivity):
    def __init__(self, driver: Remote):
        super().__init__(driver)
        self.home = Home(driver=driver)

    def launch(self):
        if not self.loaded:
            self.home.launch()
            self.home.shop_page.click()

    @property
    def loaded(self):
        return self.home.loaded and self.home.shop_page.is_selected()
