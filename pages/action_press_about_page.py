from pages.personal_page import PersonalPage


class AboutPage(PersonalPage):
    ABOUT_URL = '/about/'

    def __init__(self, page):
        super().__init__(page)

    # Селектор

    _skeleton_selector = ".col-sm-12.col-lg-9"
    _static_selector = ".static-page-h2"
    _banner_image_selector = "img[class='banner__image_content']"
    _banner_text_selector = "div[class='banner__text_content']"
    _banner_text_title_selector = "div[class='banner__text_title']"
    _content_list_image_selector = "div[class='content__list_image']"

    _content_list_selector = "div[class='content__list']"
    _list_number1_selector = "//li[@class='numbered__list_el'][1]"
    _list_number2_selector = "//li[@class='numbered__list_el'][2]"
    _list_number3_selector = "//li[@class='numbered__list_el'][3]"
    _list_number4_selector = "//li[@class='numbered__list_el'][4]"
    _list_number5_selector = "//li[@class='numbered__list_el'][5]"
    _list_number6_selector = "//li[@class='numbered__list_el'][6]"
    _list_number7_selector = "//li[@class='numbered__list_el'][7]"
    _list_number8_selector = "//li[@class='numbered__list_el'][8]"

    _content_title_selector = "h2[class='content__title']"
    _list_bottom1_selector = "//ul[contains(@class, 'content__BottomList')]/li[1]"
    _list_bottom2_selector = "//ul[contains(@class, 'content__BottomList')]/li[2]"
    _list_bottom3_selector = "//ul[contains(@class, 'content__BottomList')]/li[3]"

    _bottom_title_selector = "[class='bottom__title']"
    _bottom_devider_selector = "[class='bottom__devider']"
    _bottom_advantage1_selector = "//div[@class='bottom__advantages_block'][1]"
    _bottom_advantage2_selector = "//div[@class='bottom__advantages_block'][2]"
    _bottom_advantage3_selector = "//div[@class='bottom__advantages_block'][3]"

    # Локатор
    def skeleton_locator(self):
        return self.page.locator(self._skeleton_selector)

    def static_locator(self):
        return self.page.locator(self._static_selector)

    def banner_image_locator(self):
        return self.page.locator(self._banner_image_selector)

    def banner_text_locator(self):
        return self.page.locator(self._banner_text_selector)

    def banner_text_title_locator(self):
        return self.page.locator(self._banner_text_title_selector)

    def content_list_image_locator(self):
        return self.page.locator(self._content_list_image_selector)

    def content_list_locator(self):
        return self.page.locator(self._content_list_selector)

    def list_number1_locator(self):
        return self.page.locator(self._list_number1_selector)

    def list_number2_locator(self):
        return self.page.locator(self._list_number2_selector)

    def list_number3_locator(self):
        return self.page.locator(self._list_number3_selector)

    def list_number4_locator(self):
        return self.page.locator(self._list_number4_selector)

    def list_number5_locator(self):
        return self.page.locator(self._list_number5_selector)

    def list_number6_locator(self):
        return self.page.locator(self._list_number6_selector)

    def list_number7_locator(self):
        return self.page.locator(self._list_number7_selector)

    def list_number8_locator(self):
        return self.page.locator(self._list_number8_selector)

    def content_title_locator(self):
        return self.page.locator(self._content_title_selector)

    def list_bottom1_locator(self):
        return self.page.locator(self._list_bottom1_selector)

    def list_bottom2_locator(self):
        return self.page.locator(self._list_bottom2_selector)

    def list_bottom3_locator(self):
        return self.page.locator(self._list_bottom3_selector)

    def bottom_title_locator(self):
        return self.page.locator(self._bottom_title_selector)

    def bottom_devider_locator(self):
        return self.page.locator(self._bottom_devider_selector)

    def bottom_advantage1_locator(self):
        return self.page.locator(self._bottom_advantage1_selector)

    def bottom_advantage2_locator(self):
        return self.page.locator(self._bottom_advantage2_selector)

    def bottom_advantage3_locator(self):
        return self.page.locator(self._bottom_advantage3_selector)

    # Методы
    def visible_elements(self):
        return [self.skeleton_locator(),
                self.static_locator(),
                self.banner_image_locator(),
                self.banner_text_locator(),
                self.banner_text_title_locator(),
                self.content_list_image_locator(),
                self.content_list_locator(),
                self.list_number1_locator(),
                self.list_number2_locator(),
                self.list_number3_locator(),
                self.list_number4_locator(),
                self.list_number5_locator(),
                self.list_number6_locator(),
                self.list_number7_locator(),
                self.list_number8_locator(),
                self.content_title_locator(),
                self.list_bottom1_locator(),
                self.list_bottom2_locator(),
                self.list_bottom3_locator(),
                self.bottom_title_locator(),
                self.bottom_devider_locator(),
                self.bottom_advantage1_locator(),
                self.bottom_advantage2_locator(),
                self.bottom_advantage3_locator()]
