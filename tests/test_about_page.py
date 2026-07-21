from playwright.sync_api import expect
from utils.data import (ABOUT_URL,
                        header,
                        catalog,
                        menu_news,
                        all_news,
                        menu_advantages,
                        about_content_title,
                        about_static, about_banner_title, title_about)
from utils.hard_file import menu_news_count, menu_advantage_count, about_count


class TestAboutPage:
    def test_about_page(self, action_page, about_page, assertions):
        action_page.footer_control.click_footer_about_button()
        assertions.all_locator(about_page.header_control.collection_of_unique_locators())
        expect(about_page.header_control.header_locator()).to_have_attribute("data-qa-locator", header)
        expect(about_page.menu_catalog.catalog_locator()).to_have_text(catalog)
        assertions.all_locator(about_page.menu_catalog.collection_of_unique_locators())
        expect(about_page.menu_catalog.catalog_locator()).to_have_text(catalog)
        assertions.all_locator(about_page.menu_news.collection_of_unique_locators())
        count_elements = assertions.all_index_locator(about_page.menu_news.collections_of_repeating_locators())
        assert (assertions.all_index_locator(about_page.menu_news.collections_of_repeating_locators()) ==
                menu_news_count), f"Ожидали количество элементов {menu_news_count}! Получили: {count_elements}"
        expect(about_page.menu_news.news_locator()).to_have_text(menu_news)
        expect(about_page.menu_news.all_news_locator()).to_have_text(all_news)
        expect(about_page.menu_advantages.advantages_locator()).to_have_text(menu_advantages)
        count_elements = assertions.all_index_locator(about_page.menu_advantages.collections_of_repeating_locators())
        assert (assertions.all_index_locator(about_page.menu_advantages.collections_of_repeating_locators()) ==
                menu_advantage_count), f"Ожидали количество элементов {menu_advantage_count}! Получили:{count_elements}"
        count_elements = assertions.all_index_locator(about_page.collections_of_repeating_locators())
        assert (assertions.all_index_locator(about_page.collections_of_repeating_locators()) ==
                about_count), f"Ожидали количество элементов {menu_news_count}! Получили: {count_elements}"
        expect(about_page.content_title_locator()).to_have_text(about_content_title)
        expect(about_page.banner_text_title_locator()).to_have_text(about_banner_title)
        expect(about_page.static_locator()).to_have_text(about_static)

    def test_url_about_page(self, action_page):
        action_page.footer_control.click_footer_about_button()
        expect(action_page.page).to_have_title(title_about)
        expect(action_page.page).to_have_url(ABOUT_URL)
