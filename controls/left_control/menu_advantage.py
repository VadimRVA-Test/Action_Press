class MenuAdvantages:

    def __init__(self, page):
        self.page = page

    # селекторы
    _advantages_selector = "//span[text()='Наши преимущества']"
    _advantages_count_selector = "//span[text()='Наши преимущества']/../..//span[@class='our-adv-slant']"

    # локатор
    def advantages_locator(self):
        return self.page.locator(self._advantages_selector)

    def advantages_count_locator(self):
        return self.page.locator(self._advantages_count_selector)

    # методы
    def visible_elements(self):
        return [self.advantages_locator()]

    def list_elements(self):
        return [self.advantages_count_locator()]
