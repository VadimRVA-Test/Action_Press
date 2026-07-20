from controls.header_control import HeaderControl
from controls.left_control.menu_catalog import MenuCatalog
from controls.left_control.menu_news import MenuNews
from controls.left_control.menu_advantage import MenuAdvantages
from controls.footer_control import FooterControl
from controls.banner_control import BannerControl
from pages.base_page import BasePage


class PersonalPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.header_control = HeaderControl(self.page)
        self.menu_catalog = MenuCatalog(self.page)
        self.menu_news = MenuNews(self.page)
        self.menu_advantages = MenuAdvantages(self.page)
        self.footer_control = FooterControl(self.page)
        self.banner_control = BannerControl(self.page)
