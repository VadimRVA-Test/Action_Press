from pages.personal_page import PersonalPage


class AboutPage(PersonalPage):
    ABOUT_URL = 'about/'

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
    _content_list_count_selector = "//li[@class='numbered__list_el']"

    _content_title_selector = "h2[class='content__title']"
    _bottom_count_selector = "//ul[@class='content__BottomList']//li"

    _bottom_title_selector = "[class='bottom__title']"
    _bottom_devider_selector = "[class='bottom__devider']"
    _bottom_devider_count_selector = "[class='bottom__advantages_block']"

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

    def content_count_list_locator(self):
        return self.page.locator(self._content_list_count_selector)

    def content_title_locator(self):
        return self.page.locator(self._content_title_selector)

    def bottom_count_locator(self):
        return self.page.locator(self._bottom_count_selector)

    def bottom_title_locator(self):
        return self.page.locator(self._bottom_title_selector)

    def bottom_devider_locator(self):
        return self.page.locator(self._bottom_devider_selector)

    def bottom_devider_count_locator(self):
        return self.page.locator(self._bottom_devider_count_selector)

    # Методы
    def visible_elements(self):
        return [self.skeleton_locator(),
                self.static_locator(),
                self.banner_image_locator(),
                self.banner_text_locator(),
                self.banner_text_title_locator(),
                self.content_list_image_locator(),
                self.content_list_locator(),
                self.content_title_locator(),
                self.bottom_title_locator(),
                self.bottom_devider_locator()]

    def list_elements(self):
        return [self.content_count_list_locator(),
                self.bottom_count_locator(),
                self.bottom_devider_count_locator()]
