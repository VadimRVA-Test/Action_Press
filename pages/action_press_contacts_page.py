from pages.personal_page import PersonalPage


class ContactsPage(PersonalPage):
    CONTACTS_URL = '/about/contacts/'

    def __init__(self, page):
        super().__init__(page)

    # селекторы
    _static_page_locator = ".static-page-h2"
    _map_container_locator = ".ymaps3--map-container"
    _filial_locator = "//div[contains(@class,'filials__border_devider')][1]/.."
    _filial1_locator = "//div[contains(@class,'filials__border_devider')][1]"
    _filial1_img_locator = "//div[contains(@class,'filials__border_devider')][1]//img"
    _filial1_label_locator = "//div[contains(@class,'filials__border_devider')][1]//label"
    _filial1_contact_locator = (
        "//div[contains(@class,'filials__border_devider')][1]//div[@class='filials__block_contact']")
    _filial1_address_locator = (
        "//div[contains(@class,'filials__border_devider')][1]//div[@class='filials__block_address']")
    _filial2_locator = "//div[contains(@class,'filials__border_devider')][2]"
    _filial3_locator = "//div[contains(@class,'filials__border_devider')][3]"
    _filial4_locator = "//div[contains(@class,'filials__border_devider')][4]"
    _filial5_locator = "//div[contains(@class,'filials__block')][5]"
    _filial6_locator = "//div[contains(@class,'filials__block')][6]"

    # локаторы
    def static_page_locator(self):
        return self.element(self._static_page_locator)

    def map_container_locator(self):
        return self.element(self._map_container_locator)

    def filial_locator(self):
        return self.element(self._filial_locator)

    def filial1_locator(self):
        return self.element(self._filial1_locator)

    def filial1_img_locator(self):
        return self.element(self._filial1_img_locator)

    def filial1_label_locator(self):
        return self.element(self._filial1_label_locator)

    def filial1_contact_locator(self):
        return self.element(self._filial1_contact_locator)

    def filial1_address_locator(self):
        return self.element(self._filial1_address_locator)

    def filial2_locator(self):
        return self.element(self._filial2_locator)

    def filial3_locator(self):
        return self.element(self._filial3_locator)

    def filial4_locator(self):
        return self.element(self._filial4_locator)

    def filial5_locator(self):
        return self.element(self._filial5_locator)

    def filial6_locator(self):
        return self.element(self._filial6_locator)

    # методы
    def visible_elements(self):
        return [self.static_page_locator(),
                self.map_container_locator(),
                self.filial_locator(),
                self.filial1_locator(),
                self.filial1_img_locator(),
                self.filial1_label_locator(),
                self.filial1_contact_locator(),
                self.filial1_address_locator(),
                self.filial2_locator(),
                self.filial3_locator(),
                self.filial4_locator(),
                self.filial5_locator(),
                self.filial6_locator()]
