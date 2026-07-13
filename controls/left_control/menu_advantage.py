class MenuAdvantages:

    def __init__(self, page):
        self.page = page

    # селекторы
    _advantages_selector = "//span[text()='Наши преимущества']"
    _advantage1_selector = "//span[contains(text(), 'Профессиональные знания')]"
    _advantage2_selector = "//span[text()='Работаем с 1994 года']"
    _advantage3_selector = "//span[text()='Более 5000 сотрудников']"
    _advantage4_selector = "//span[text()='Более 5000 сотрудников']"
    _advantage5_selector = "//span[text()='Более 5000 сотрудников']"

    # локатор
    def advantages_locator(self):
        return self.page.locator(self._advantages_selector)

    def advantage1_locator(self):
        return self.page.locator(self._advantage1_selector)

    def advantage2_locator(self):
        return self.page.locator(self._advantage2_selector)

    def advantage3_locator(self):
        return self.page.locator(self._advantage3_selector)

    def advantage4_locator(self):
        return self.page.locator(self._advantage4_selector)

    def advantage5_locator(self):
        return self.page.locator(self._advantage5_selector)

    # методы
    def visible_elements(self):
        return [self.advantages_locator(),
                self.advantage1_locator(),
                self.advantage2_locator(),
                self.advantage3_locator(),
                self.advantage4_locator(),
                self.advantage5_locator()]
