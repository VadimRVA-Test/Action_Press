from pages.personal_page import PersonalPage


class ActionPressPage(PersonalPage):
    PAGE_URL = PersonalPage.BASE_URL

    def __init__(self, page):
        super().__init__(page)
        self.page = page

    # селекторы
    _skeleton_selector = ".col-lg-9"

    _recommended_publications_selector = ".title-text"

    _recommendation1_selector = "//div[contains(@class,'order-12')]"
    _image_recommendation1_selector = "//div[contains(@class,'order-12')]//img[@class='card-img-top']"
    _card_title_rec1_selector = "//div[contains(@class,'order-12')]//a[@class='card-title']"
    _card_text_catalog_rec1_selector = "//div[contains(@class,'order-12')]//p[@class='card-text-catalog']"
    _price_zone_selector = "//div[contains(@class,'order-12')]//div[contains(@class,'price-zone')]"
    _button_box_selector = "//div[contains(@class,'order-12')]//div[contains(@class,'price-zone')]//button"

    # локаторы
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

    def card_text_catalog_rec1_locator(self):
        return self.element(self._card_text_catalog_rec1_selector)

    def price_zone_locator(self):
        return self.element(self._price_zone_selector)

    def button_box_locator(self):
        return self.element(self._button_box_selector)

    # методы
    def collection_of_unique_locator(self):
        return [self.skeleton_locator(),
                self.recommended_publications_locator()]

    def collections_of_repeating_locators(self):
        return [self.recommendation1_locator(),
                self.image_recommendation1_locator(),
                self.card_title_rec1_locator(),
                self.card_text_catalog_rec1_locator(),
                self.price_zone_locator(),
                self.button_box_locator()]
