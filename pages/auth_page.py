from pages.personal_page import PersonalPage


class AuthPage(PersonalPage):
    AUTH_URL = "https://id2.action-media.ru/logon/index?reglink=https"

    # селекторы
    _wrapper_selector = ".Wrapper_mobileWrapper__aQXiW"

    _logo_header_selector = ".FormTitle_title__Qp9FV"
    _logo_selector = ".LocalizedLogo_logoRU__6lWNu"

    _label_mail_selector = "//input[@name='login']/..//label"
    _input_login_selector = "[name='login']"

    _pass_selector = "//label[text()='Пароль']"
    _input_pass_selector = "[name='password']"

    _button_remind_selector = ".Button2_inline__H9NxX"
    _button_enter_selector = ".SubmitButton_submitButton__RtIt6"

    _button_registration_selector = ".RegistrationButton_createAccButton__LKi8l"

    _title_supports_selector = ".SocialButtons_socialAuthHeader__10RVn"
    _button_vk_selector = "[data-qa-locator='vk-auth']"
    _button_mail_selector = "[data-qa-locator='mailru-auth']"
    _button_classmates_selector = "[data-qa-locator='ok-auth']"
    _button_yandex_selector = "[data-qa-locator='yandex-auth']"

    _phone_locator = ".Copyright_phone__8izzP"
    _copyright_icon_selector = ".Copyright_copyrightText__yPT_Z"

    # локаторы
    def wrapper_locator(self):
        return self.element(self._wrapper_selector)

    def logo_header_locator(self):
        return self.element(self._logo_header_selector)

    def logo_locator(self):
        return self.element(self._logo_selector)

    def label_mail_locator(self):
        return self.element(self._label_mail_selector)

    def input_login_locator(self):
        return self.element(self._input_login_selector)

    def pass_locator(self):
        return self.element(self._pass_selector)

    def input_pass_locator(self):
        return self.element(self._input_pass_selector)

    def button_remind_locator(self):
        return self.element(self._button_remind_selector)

    def button_enter_locator(self):
        return self.element(self._button_enter_selector)

    def button_registration_locator(self):
        return self.element(self._button_registration_selector)

    def title_supports_locator(self):
        return self.element(self._title_supports_selector)

    def button_vk_locator(self):
        return self.element(self._button_vk_selector)

    def button_mail_locator(self):
        return self.element(self._button_mail_selector)

    def button_classmates_locator(self):
        return self.element(self._button_classmates_selector)

    def button_yandex_locator(self):
        return self.element(self._button_yandex_selector)

    def phone_locator(self):
        return self.element(self._phone_locator)

    def copyright_icon_locator(self):
        return self.element(self._copyright_icon_selector)

    # методы
    def fill_login(self, mail):
        self.input_login_locator().fill(mail)

    def fill_password(self, password):
        self.input_pass_locator().fill(password)

    def click_enter(self):
        self.button_enter_locator().click()

    # комбинированные методы
    def collection_of_unique_locator(self):
        return [self.wrapper_locator(),
                self.logo_header_locator(),
                self.logo_locator(),
                self.label_mail_locator(),
                self.input_login_locator(),
                self.pass_locator(),
                self.input_pass_locator(),
                self.button_remind_locator(),
                self.button_enter_locator(),
                self.button_registration_locator(),
                self.title_supports_locator(),
                self.button_vk_locator(),
                self.button_mail_locator(),
                self.button_classmates_locator(),
                self.button_yandex_locator(),
                self.phone_locator(),
                self.copyright_icon_locator()]

    def authorize(self, mail, password):
        self.fill_login(mail)
        self.fill_password(password)
        self.click_enter()
