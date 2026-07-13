from pages.personal_page import PersonalPage


class PaymentPage(PersonalPage):
    PAYMENT_URL = '/about/payment/'

    def __init__(self, page):
        super().__init__(page)

    # селекторы
    _skeleton_locator = ".col-lg-9"
    _static_page_locator = ".static-page-h2"

    _payment_non_cash_locator = "//div[contains(@class,'col-lg-9')]//div[@class='payment__card'][1]"
    _payment_non_cash_img_locator = (
        "//div[contains(@class,'col-lg-9')]//div[@class='payment__card'][1]//div[@class='payment__img']")
    _payment_description_locator = (
        "//div[contains(@class,'col-lg-9')]//div[@class='payment__card'][1]//div[@class='payment__descr-text'][1]")

    _payment_cash_locator = "//div[contains(@class,'col-lg-9')]//div[@class='payment__card'][2]"
    _payment_card_locator = "//div[contains(@class,'col-lg-9')]//div[@class='payment__card'][3]"

    _refound_locator = "div[class='refund']"

    # локаторы
    def skeleton_locator(self):
        return self.element(self._skeleton_locator)

    def static_page_locator(self):
        return self.element(self._static_page_locator)

    def payment_non_cash_locator(self):
        return self.element(self._payment_non_cash_locator)

    def payment_non_cash_img_locator(self):
        return self.element(self._payment_non_cash_img_locator)

    def payment_description_locator(self):
        return self.element(self._payment_description_locator)

    def payment_cash_locator(self):
        return self.element(self._payment_cash_locator)

    def payment_card_locator(self):
        return self.element(self._payment_card_locator)

    def refound_locator(self):
        return self.element(self._refound_locator)

    # методы
    def visible_elements(self):
        return [self.skeleton_locator(),
                self.static_page_locator(),
                self.payment_non_cash_locator(),
                self.payment_non_cash_img_locator(),
                self.payment_description_locator(),
                self.payment_cash_locator(),
                self.payment_card_locator(),
                self.refound_locator()]
