class MenuNews:

    def __init__(self, page):
        self.page = page

    # селекторы
    _news_selector = "//span[text()='Новости']"
    _news1_selector = "//li[@data-qa-locator='newsLink'][1]"
    _news2_selector = "//li[@data-qa-locator='newsLink'][2]"
    _news3_selector = "//li[@data-qa-locator='newsLink'][3]"
    _news4_selector = "//li[@data-qa-locator='newsLink'][4]"
    _all_news_selector = "[href='/news/']"

    # локатор
    def news_selector_locator(self):
        return self.page.locator(self._news_selector)

    def news1_selector_locator(self):
        return self.page.locator(self._news1_selector)

    def news2_selector_locator(self):
        return self.page.locator(self._news2_selector)

    def news3_selector_locator(self):
        return self.page.locator(self._news3_selector)

    def news4_selector_locator(self):
        return self.page.locator(self._news4_selector)

    def all_news_locator(self):
        return self.page.locator(self._all_news_selector)

    # методы
    def visible_elements(self):
        return [self.news_selector_locator(),
                self.news1_selector_locator(),
                self.news2_selector_locator(),
                self.news3_selector_locator(),
                self.news4_selector_locator(),
                self.all_news_locator()]
