class MenuAdvantages:

    def __init__(self, page):
        self.page = page

    # селекторы
    _advantages_selector = "//span[text()='Наши преимущества']"
    _advantages_count_selector = "//span[text()='Наши преимущества']/../..//li"

    # локаторы
    def advantages_locator(self):
        return self.page.locator(self._advantages_selector)

    def advantages_count_locator(self):
        return self.page.locator(self._advantages_count_selector)

    # методы
    def collection_of_unique_locators(self):
        return [self.advantages_locator()]

    def collections_of_repeating_locators(self):
        return [self.advantages_count_locator()]
