from playwright.sync_api import expect
from utils.data import CONTACT_URL, header, catalog, menu_news, all_news, menu_advantages, contacts1, title_contacts
from utils.hard_file import contact_count, menu_news_count, menu_advantage_count


class TestContactPage:
    def test_contacts_page(self, action_page, contacts_page, assertions):
        action_page.footer_control.click_footer_contacts_button()
        assertions.all_locator(contacts_page.header_control.collection_of_unique_locators())
        expect(contacts_page.header_control.header_locator()).to_have_attribute("data-qa-locator", header)
        expect(contacts_page.menu_catalog.catalog_locator()).to_have_text(catalog)
        assertions.all_locator(contacts_page.menu_catalog.collection_of_unique_locators())
        expect(contacts_page.menu_catalog.catalog_locator()).to_have_text(catalog)
        assertions.all_locator(contacts_page.menu_news.collection_of_unique_locators())
        count_elements = assertions.all_index_locator(contacts_page.menu_news.collections_of_repeating_locators())
        assert (assertions.all_index_locator(contacts_page.menu_news.collections_of_repeating_locators()) ==
                menu_news_count), f"Ожидали количество элементов {menu_news_count}! Получили: {count_elements}"
        expect(contacts_page.menu_news.news_locator()).to_have_text(menu_news)
        expect(contacts_page.menu_news.all_news_locator()).to_have_text(all_news)
        expect(contacts_page.menu_advantages.advantages_locator()).to_have_text(menu_advantages)
        count_elements = (
            assertions.all_index_locator(contacts_page.menu_advantages.collections_of_repeating_locators()))
        assert (assertions.all_index_locator(contacts_page.menu_advantages.collections_of_repeating_locators()) ==
                menu_advantage_count), f"Ожидали количество элементов {menu_news_count}! Получили: {count_elements}"
        assertions.all_locator(contacts_page.collection_of_unique_locators())
        count_element = assertions.all_index_locator(contacts_page.collections_of_repeating_locators())
        assert count_element == contact_count, f"Ожидали количество элементов{contact_count}!Получили:{count_element}"
        expect(contacts_page.static_page_locator()).to_have_text(contacts1)

    def test_url_contacts_page(self, action_page):
        action_page.footer_control.click_footer_contacts_button()
        expect(action_page.page).to_have_title(title_contacts)
        expect(action_page.page).to_have_url(CONTACT_URL)
