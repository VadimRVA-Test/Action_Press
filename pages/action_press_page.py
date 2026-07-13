from pages.personal_page import PersonalPage


class ActionPressPage(PersonalPage):
    PAGE_URL = PersonalPage.BASE_URL

    def __init__(self, page):
        super().__init__(page)

    # Селекторы
    _skeleton_selector = ".col-lg-9"

    _recommended_publications_selector = ".title-text"

    _recommendation1_selector = "//div[contains(@class,'order-12')][1]"
    _image_recommendation1_selector = "//div[contains(@class,'order-12')][1]//img[@class='card-img-top']"
    _card_title_rec1_selector = "//div[contains(@class,'order-12')][1]//a[@class='card-title']"
    _card_text_catalog_rec1_selector = "//div[contains(@class,'order-12')][1]//p[@class='card-text-catalog']"
    _price_zone_selector = "//div[contains(@class,'order-12')][1]//div[contains(@class,'price-zone')]"
    _button_box_selector = "//div[contains(@class,'order-12')][1]//div[contains(@class,'price-zone')]//button"

    _recommendation2_selector = "//div[contains(@class,'order-12')][2]"
    _recommendation3_selector = "//div[contains(@class,'order-12')][3]"
    _recommendation4_selector = "//div[contains(@class,'order-12')][4]"
    _recommendation5_selector = "//div[contains(@class,'order-12')][5]"
    _recommendation6_selector = "//div[contains(@class,'order-12')][6]"
    _recommendation7_selector = "//div[contains(@class,'order-12')][7]"
    _recommendation8_selector = "//div[contains(@class,'order-12')][8]"
    _recommendation9_selector = "//div[contains(@class,'order-12')][9]"
    _recommendation10_selector = "//div[contains(@class,'order-12')][10]"
    _recommendation11_selector = "//div[contains(@class,'order-12')][11]"
    _recommendation12_selector = "//div[contains(@class,'order-12')][12]"
    _recommendation13_selector = "//div[contains(@class,'order-12')][13]"
    _recommendation14_selector = "//div[contains(@class,'order-12')][14]"
    _recommendation15_selector = "//div[contains(@class,'order-12')][15]"
    _recommendation16_selector = "//div[contains(@class,'order-12')][16]"
    _recommendation17_selector = "//div[contains(@class,'order-12')][17]"
    _recommendation18_selector = "//div[contains(@class,'order-12')][18]"

    # Локаторы
    def skeleton_locator(self):
        return self.element(self._skeleton_selector)

    def recommended_publications_locator(self):
        return self.element(self._recommended_publications_selector)

    def recommendation1_locator(self):
        return self.element(self._recommendation1_selector)

    def image_recommendation1_locator(self):
        return self.element(self._recommendation1_selector)

    def card_title_rec1_locator(self):
        return self.element(self._card_title_rec1_selector)

    def price_zone_locator(self):
        return self.element(self._price_zone_selector)

    def button_box_locator(self):
        return self.element(self._button_box_selector)

    def recommendation2_locator(self):
        return self.element(self._recommendation2_selector)

    def recommendation3_locator(self):
        return self.element(self._recommendation3_selector)

    def recommendation4_locator(self):
        return self.element(self._recommendation4_selector)

    def recommendation5_locator(self):
        return self.element(self._recommendation5_selector)

    def recommendation6_locator(self):
        return self.element(self._recommendation6_selector)

    def recommendation7_locator(self):
        return self.element(self._recommendation7_selector)

    def recommendation8_locator(self):
        return self.element(self._recommendation8_selector)

    def recommendation9_locator(self):
        return self.element(self._recommendation9_selector)

    def recommendation10_locator(self):
        return self.element(self._recommendation10_selector)

    def recommendation11_locator(self):
        return self.element(self._recommendation11_selector)

    def recommendation12_locator(self):
        return self.element(self._recommendation12_selector)

    def recommendation13_locator(self):
        return self.element(self._recommendation13_selector)

    def recommendation14_locator(self):
        return self.element(self._recommendation14_selector)

    def recommendation15_locator(self):
        return self.element(self._recommendation15_selector)

    def recommendation16_locator(self):
        return self.element(self._recommendation16_selector)

    def recommendation17_locator(self):
        return self.element(self._recommendation17_selector)

    def recommendation18_locator(self):
        return self.element(self._recommendation18_selector)

    # Методы
    def visible_elements(self):
        return [self.skeleton_locator(),
                self.recommended_publications_locator(),
                self.recommendation1_locator(),
                self.image_recommendation1_locator(),
                self.card_title_rec1_locator(),
                self.price_zone_locator(),
                self.button_box_locator(),
                self.recommendation2_locator(),
                self.recommendation3_locator(),
                self.recommendation4_locator(),
                self.recommendation5_locator(),
                self.recommendation6_locator(),
                self.recommendation7_locator(),
                self.recommendation8_locator(),
                self.recommendation9_locator(),
                self.recommendation10_locator(),
                self.recommendation11_locator(),
                self.recommendation12_locator(),
                self.recommendation13_locator(),
                self.recommendation14_locator(),
                self.recommendation15_locator(),
                self.recommendation16_locator(),
                self.recommendation17_locator(),
                self.recommendation18_locator()]
