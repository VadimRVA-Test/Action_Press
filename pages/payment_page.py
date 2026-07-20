from pages.personal_page import PersonalPage


class PaymentPage(PersonalPage):
    PAYMENT_URL = 'about/payment/'

    def __init__(self, page):
        super().__init__(page)

    # селекторы
    _skeleton_selector = ".col-lg-9"
    _static_page_selector = ".static-page-h2"
    _non_cash_text_selector = "//h3[normalize-space(text())='Безналичный платеж']"
    _cash_text_selector = "//h3[normalize-space(text())='Наличный платеж']"
    _card_text_selector = "//h3[normalize-space(text())='Оплата банковской картой']"
    _refound_text_selector = "//h2[normalize-space(text())='Возврат денежных средств']"

    _payment_non_cash_selector = "//div[@class='payment__card']"
    _payment_non_cash_img_selector = "//div[@class='payment__img']"
    _payment_title_selector = "//h3[@class='payment__descr-title']"
    _payment_description_selector = "//div[@class='payment__descr-text']"

    _payment_description_img_selector = "//div[@class='payment__descr-img']"

    _refound_selector = "div[class='refund']"
    _refound_list_selector = "//ul[@class='refund-list']//li"

    # локаторы
    def skeleton_locator(self):
        return self.element(self._skeleton_selector)

    def static_page_locator(self):
        return self.element(self._static_page_selector)

    def non_cash_text_locator(self):
        return self.element(self._non_cash_text_selector)

    def cash_text_locator(self):
        return self.element(self._cash_text_selector)

    def card_text_locator(self):
        return self.element(self._card_text_selector)

    def refound_text_locator(self):
        return self.element(self._refound_text_selector)

    def payment_non_cash_locator(self):
        return self.element(self._payment_non_cash_selector)

    def payment_non_cash_img_locator(self):
        return self.element(self._payment_non_cash_img_selector)

    def payment_title_locator(self):
        return self.element(self._payment_title_selector)

    def payment_description_locator(self):
        return self.element(self._payment_description_selector)

    def payment_description_img_locator(self):
        return self.element(self._payment_description_img_selector)

    def refound_locator(self):
        return self.element(self._refound_selector)

    def refound_list_locator(self):
        return self.element(self._refound_list_selector)

    # методы
    def collection_of_unique_locators(self):
        return [self.skeleton_locator(),
                self.static_page_locator(),
                self.payment_description_img_locator(),
                self.refound_locator()]

    def collections_of_repeating_locators(self):
        return [self.payment_non_cash_locator(),
                self.payment_non_cash_img_locator(),
                self.payment_title_locator(),
                self.payment_description_locator(),
                self.refound_list_locator()]
