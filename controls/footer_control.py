class FooterControl:

    def __init__(self, page):
        self.page = page

    # селекторы
    _footer_about_button_selector = "//div[contains(@class,'plf-6')]//a[@href='/about/']"
    _footer_contacts_button_selector = "//div[contains(@class,'plf-6')]//a[@href='/about/contacts/']"
    _footer_payment_button_selector = "//div[contains(@class,'plf-6')]//a[@href='/about/payment/']"

    # локаторы
    def footer_about_button_locator(self):
        return self.page.locator(self._footer_about_button_selector)

    def footer_contacts_button_locator(self):
        return self.page.locator(self._footer_contacts_button_selector)

    def footer_payment_button_locator(self):
        return self.page.locator(self._footer_payment_button_selector)

    # методы
    def click_footer_about_button(self):
        self.footer_about_button_locator().click()

    def click_footer_contacts_button(self):
        self.footer_contacts_button_locator().click()

    def click_footer_payment_button(self):
        self.footer_payment_button_locator().click()
