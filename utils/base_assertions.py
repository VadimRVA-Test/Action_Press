from playwright.sync_api import expect
from pages.personal_page import PersonalPage
from utils.data import header, catalog, menu_news, all_news, menu_advantages
from utils.hard_file import menu_news_count, menu_advantage_count


class Assertions:
    def __init__(self, page):
        self.page = page

    @staticmethod
    def all_locators(locators):
        for locator in locators:
            expect(locator).to_be_visible()

    @staticmethod
    def all_index_locators(locators):
        index_locator = 0
        for locator in locators:
            for value in range(locator.count()):
                expect(locator.nth(value)).to_be_visible()
                index_locator += 1
        return index_locator

    @staticmethod
    def assert_elements_count(locators, expected_count, block_name):
        actual_count = Assertions.all_index_locators(locators)
        assert actual_count == expected_count, (
            f"[{block_name} Ожидали {expected_count} элементов, получили {actual_count}")

    def base_assertions(self, page: PersonalPage):
        # header
        self.all_locators(page.header_control.collection_of_unique_locators())
        expect(page.header_control.header_locator()).to_have_attribute("src", header)
        # catalog
        self.all_locators(page.menu_catalog.collection_of_unique_locators())
        expect(page.menu_catalog.catalog_locator()).to_have_text(catalog)
        # news
        self.all_locators(page.menu_news.collection_of_unique_locators())
        self.assert_elements_count(
            page.menu_news.collections_of_repeating_locators(),
            menu_news_count,
            "menu_news")
        expect(page.menu_news.news_locator()).to_have_text(menu_news)
        expect(page.menu_news.all_news_locator()).to_have_text(all_news)
        # advantages
        self.all_locators(page.menu_advantages.collection_of_unique_locators())
        self.assert_elements_count(
            page.menu_advantages.collections_of_repeating_locators(),
            menu_advantage_count,
            "menu_advantages")
        expect(page.menu_advantages.advantages_locator()).to_have_text(menu_advantages)
