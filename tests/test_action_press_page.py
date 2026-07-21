from playwright.sync_api import expect
from utils.data import menu_news, all_news, menu_advantages, URl, action, catalog, header, title_action
from utils.hard_file import menu_news_count, menu_advantage_count, action_count


class TestActionPage:
    def test_action_press_page(self, action_page, assertions):
        assertions.all_locator(action_page.header_control.collection_of_unique_locators())
        expect(action_page.header_control.header_locator()).to_have_attribute("data-qa-locator", header)
        expect(action_page.menu_catalog.catalog_locator()).to_have_text(catalog)
        assertions.all_locator(action_page.menu_catalog.collection_of_unique_locators())
        expect(action_page.menu_catalog.catalog_locator()).to_have_text(catalog)
        assertions.all_locator(action_page.menu_news.collection_of_unique_locators())
        count_elements = assertions.all_index_locator(action_page.menu_news.collections_of_repeating_locators())
        assert (assertions.all_index_locator(action_page.menu_news.collections_of_repeating_locators()) ==
                menu_news_count), f"Ожидали количество элементов {menu_news_count}! Получили: {count_elements}"
        expect(action_page.menu_news.news_locator()).to_have_text(menu_news)
        expect(action_page.menu_news.all_news_locator()).to_have_text(all_news)
        expect(action_page.menu_advantages.advantages_locator()).to_have_text(menu_advantages)
        count_elements = assertions.all_index_locator(action_page.menu_advantages.collections_of_repeating_locators())
        assert (assertions.all_index_locator(action_page.menu_advantages.collections_of_repeating_locators()) ==
                menu_advantage_count), f"Ожидали количество элементов {menu_news_count}! Получили: {count_elements}"
        assertions.all_locator(action_page.collection_of_unique_locator())
        count_elements = assertions.all_index_locator(action_page.collections_of_repeating_locators())
        assert (assertions.all_index_locator(action_page.collections_of_repeating_locators()) ==
                action_count), f"Ожидали количество элементов {action_count}! Получили: {count_elements}"
        expect(action_page.recommended_publications_locator()).to_have_text(action)

    def test_url_action_page(self, action_page):
        expect(action_page.page).to_have_title(title_action)
        expect(action_page.page).to_have_url(URl)
