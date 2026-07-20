from pages.personal_page import PersonalPage


class ContactsPage(PersonalPage):
    CONTACTS_URL = 'about/contacts/'

    def __init__(self, page):
        super().__init__(page)

    # селекторы
    _static_page_selector = ".static-page-h2"
    _map_container_selector = ".ymaps3--map-container"

    _filials_count_selector = ".filials"
    _filial_count_devider_selector = "//div[contains(@class,'filials__border_devider')]"
    _filial_count_img_selector = "//div[contains(@class,'filials__block')]//img"
    _filial_count_label_selector = "//label[@class='filials__block_label']"
    _filial_count_contact_selector = "//div[@class='filials__block_contact']"
    _filial_count_address_selector = "//div[@class='filials__block_address']"
    _filial_count_devider2_selector = "//div[@class='filials']//div[(@class='filials__block')]"

    _filial_count_feedbeak_selector = "label[class='feedback__title']"
    _filial_count_mess_selector = "div[class='feedback__messengers_element']"

    _profit_selector = (
        "[href='https://www.proflit.ru/?utm_source=action-press&utm_campaign=action-press&utm_content=action-press']")
    _seminar_selector = (
        "[href='https://www.seminar.ru/?utm_source=action-press&utm_campaign=action-press&utm_content=action-press']")

    # локаторы
    def static_page_locator(self):
        return self.element(self._static_page_selector)

    def map_container_locator(self):
        return self.element(self._map_container_selector)

    def filials_count_locator(self):
        return self.element(self._filials_count_selector)

    def filial_count_devider_locator(self):
        return self.element(self._filial_count_devider_selector)

    def filial_count_devider2_locator(self):
        return self.element(self._filial_count_devider2_selector)

    def filial_count_img_locator(self):
        return self.element(self._filial_count_img_selector)

    def filial_count_label_locator(self):
        return self.element(self._filial_count_label_selector)

    def filial_count_contact_locator(self):
        return self.element(self._filial_count_contact_selector)

    def filial_count_address_locator(self):
        return self.element(self._filial_count_address_selector)

    def filial_count_feedbeak_locator(self):
        return self.element(self._filial_count_feedbeak_selector)

    def filial_count_mess_locator(self):
        return self.element(self._filial_count_mess_selector)

    def profit_locator(self):
        return self.element(self._profit_selector)

    def seminar_locator(self):
        return self.element(self._seminar_selector)

    # методы
    def collection_of_unique_locators(self):
        return [self.static_page_locator(),
                self.map_container_locator(),
                self.filials_count_locator(),
                self.profit_locator(),
                self.seminar_locator()]

    def collections_of_repeating_locators(self):
        return [self.filial_count_devider_locator(),
                self.filial_count_devider2_locator(),
                self.filial_count_img_locator(),
                self.filial_count_label_locator(),
                self.filial_count_contact_locator(),
                self.filial_count_address_locator(),
                self.filial_count_feedbeak_locator(),
                self.filial_count_mess_locator()]
