from playwright.sync_api import Page
from controls.banner_control import BannerControl


class BasePage:
    BASE_URL = "https://action-press.ru/"

    def __init__(self, page: Page):
        self.page = page

    def composite_url(self, url=None):
        if url:
            return f"{self.BASE_URL}{url}"
        else:
            return f"{self.BASE_URL}"

    def open_page(self, url=None):
        self.page.goto(self.composite_url(url))
        cookies = BannerControl(self.page).accept_cookies_button_locator()
        jiva = BannerControl(self.page).close_jiva_button_locator()
        if cookies.is_visible():
            cookies.click()
        elif jiva.is_visible():
            jiva.click()
        else:
            pass

    def element(self, selector):
        return self.page.locator(selector)
