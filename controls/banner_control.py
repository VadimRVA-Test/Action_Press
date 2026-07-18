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
