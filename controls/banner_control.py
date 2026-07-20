class BannerControl:

    def __init__(self, page):
        self.page = page

    # селекторы
    _close_jiva_button_selector = "#jivo_close_button"
    _accept_cookies_button_selector = ".btn.btn-primary"

    # локаторы
    def close_jiva_button_locator(self):
        return self.page.locator(self._close_jiva_button_selector)

    def accept_cookies_button_locator(self):
        return self.page.locator(self._accept_cookies_button_selector)

    # методы
    def click_close_jiva(self):
        self.close_jiva_button_locator().click()

    def click_accept_cookies(self):
        self.accept_cookies_button_locator().click()
