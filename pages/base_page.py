from playwright.sync_api import Page


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

    def element(self, selector):
        return self.page.locator(selector)
