class MenuNews:

    def __init__(self, page):
        self.page = page

    # селекторы
    _news_selector = "//span[text()='Новости']"
    _news_count_selector = "//span[text()='Новости']/../..//li[@data-qa-locator='newsLink']"
    _all_news_selector = "[href='/news/']"

    # локатор
    def news_locator(self):
        return self.page.locator(self._news_selector)

    def news_count_locator(self):
        return self.page.locator(self._news_count_selector)

    def all_news_locator(self):
        return self.page.locator(self._all_news_selector)

    # методы
    def visible_elements(self):
        return [self.news_locator(),
                self.all_news_locator()]

    def list_elements(self):
        return [self.news_count_locator()]
