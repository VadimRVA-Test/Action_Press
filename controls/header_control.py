class HeaderControl:
    def __init__(self, page):
        self.page = page

    # селекторы
    _skeleton_locator = ".navbar-light"
    _header_selector = ".navbar-brand"

    _phone_selector = "div[data-qa-locator='phoneNumber']"

    _telegram_selector = ".telegramm_ico"
    _whatsapp_selector = ".whats_ico"
    _max_selector = ".max_ico"

    _button_auth_reg_selector = ".authButton_button__jBFUH"
    _profile_name_selector = ".authButton_buttonText__wGjvY"

    _button_product_selector = "//ul[@class='Dropdown__navigationList--Onlwi']//li[1]"
    _button_close_doc_selector = "//ul[@class='Dropdown__navigationList--Onlwi']//li[2]"
    _button_activation_selector = "//ul[@class='Dropdown__navigationList--Onlwi']//li[3]"
    _button_useful_selector = "//ul[@class='Dropdown__navigationList--Onlwi']//li[4]"
    _button_support_selector = "//ul[@class='Dropdown__navigationList--Onlwi']//li[5]"
    _button_profile_selector = "//ul[@class='Dropdown__navigationList--Onlwi']//li[6]"
    _button_exit_auth = "//a[contains(@class,'Dropdown__logoutButton--94Zp7')]"

    _basket_product_selector = "//a[contains(@class, 'basket-item')]"

    _about_selector = "//a[contains(@class, 'sub-header-btn') and @href='/about/']"
    _contacts_selector = "//a[contains(@class, 'sub-header-btn') and @href='/about/contacts/']"
    _payment_selector = "//a[contains(@class, 'sub-header-btn') and @href='/about/payment/']"
    _deliver_selector = "//a[contains(@class, 'sub-header-btn') and @href='/about/deliver/']"

    _search_selector = "//div[@class='col-2-sub']//input[contains(@class,'form-control-sub-header')]"

    _search2_selector = "[placeholder='Что вы хотите найти?']"
    _fluid_selector = ".img-fluid"
    _search_button_selector = ".l-ss-c-button.l-ss-c-search-input-action-search"
    _result_selector = ".l-ss-c-text-caption"

    # локатор
    def skeleton_locator(self):
        return self.page.locator(self._skeleton_locator)

    def header_locator(self):
        return self.page.locator(self._header_selector)

    def phone_locator(self):
        return self.page.locator(self._phone_selector)

    def telegram_locator(self):
        return self.page.locator(self._telegram_selector)

    def whatsapp_locator(self):
        return self.page.locator(self._whatsapp_selector)

    def max_locator(self):
        return self.page.locator(self._max_selector)

    def button_auth_reg_locator(self):
        return self.page.locator(self._button_auth_reg_selector)

    def profile_name_locator(self):
        return self.page.locator(self._profile_name_selector)

    def button_product_locator(self):
        return self.page.locator(self._button_product_selector)

    def button_close_doc_locator(self):
        return self.page.locator(self._button_close_doc_selector)

    def button_activation_locator(self):
        return self.page.locator(self._button_activation_selector)

    def button_useful_locator(self):
        return self.page.locator(self._button_useful_selector)

    def button_support_locator(self):
        return self.page.locator(self._button_support_selector)

    def button_profile_locator(self):
        return self.page.locator(self._button_profile_selector)

    def button_exit_auth(self):
        return self.page.locator(self._button_exit_auth)

    def basket_product_locator(self):
        return self.page.locator(self._basket_product_selector)

    def about_locator(self):
        return self.page.locator(self._about_selector)

    def contacts_locator(self):
        return self.page.locator(self._contacts_selector)

    def payment_locator(self):
        return self.page.locator(self._payment_selector)

    def deliver_locator(self):
        return self.page.locator(self._deliver_selector)

    def search_locator(self):
        return self.page.locator(self._search_selector)

    def search2_locator(self):
        return self.page.locator(self._search2_selector)

    def fluid_locator(self):
        return self.page.locator(self._fluid_selector)

    def search_button_locator(self):
        return self.page.locator(self._search_button_selector)

    def result_locator(self):
        return self.page.locator(self._result_selector)

    # методы
    def search(self, data):
        self.search2_locator().fill(data)
        return self.search2_locator()

    def visible_elements(self):
        return [self.skeleton_locator(),
                self.header_locator(),
                self.phone_locator(),
                self.telegram_locator(),
                self.whatsapp_locator(),
                self.max_locator(),
                self.button_auth_reg_locator(),
                self.profile_name_locator(),
                self.basket_product_locator(),
                self.about_locator(),
                self.contacts_locator(),
                self.payment_locator(),
                self.deliver_locator(),
                self.search_locator()]

    def profile_button(self):
        return [self.button_product_locator(),
                self.button_close_doc_locator(),
                self.button_activation_locator(),
                self.button_useful_locator(),
                self.button_support_locator(),
                self.button_profile_locator(),
                self.button_exit_auth()]
