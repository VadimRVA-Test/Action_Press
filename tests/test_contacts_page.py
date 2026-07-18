from playwright.sync_api import expect
from utils.data import CONTACT_URL, header, catalog, menu_news, all_news, menu_advantages, contacts1
from utils.hard_file import contact_count, menu_news_count, menu_advantage_count


def test_contacts_page(action_page, contacts_page, assertions):
    action_page.footer_control.footer_contacts_button_locator().click()
    contacts_page.page = action_page.page
    expect(contacts_page.page).to_have_url(CONTACT_URL)
    assertions.all_locator(contacts_page.header_control.visible_elements())
    expect(contacts_page.header_control.header_locator()).to_have_attribute("data-qa-locator", header)
    expect(contacts_page.menu_catalog.catalog_locator()).to_have_text(catalog)
    assertions.all_locator(contacts_page.menu_catalog.visible_elements())
    expect(contacts_page.menu_catalog.catalog_locator()).to_have_text(catalog)
    assertions.all_locator(contacts_page.menu_news.visible_elements())
    count_elements = assertions.all_index_locator(contacts_page.menu_news.list_elements())
    assert assertions.all_index_locator(contacts_page.menu_news.list_elements()) == menu_news_count, (
        f"Ожидали количество элементов {menu_news_count}! Получили: {count_elements}")
    expect(contacts_page.menu_news.news_locator()).to_have_text(menu_news)
    expect(contacts_page.menu_news.all_news_locator()).to_have_text(all_news)
    expect(contacts_page.menu_advantages.advantages_locator()).to_have_text(menu_advantages)
    count_elements2 = assertions.all_index_locator(contacts_page.menu_advantages.list_elements())
    assert assertions.all_index_locator(contacts_page.menu_advantages.list_elements()) == menu_advantage_count, (
        f"Ожидали количество элементов {menu_news_count}! Получили: {count_elements2}")
    assertions.all_locator(contacts_page.visible_elements())
    count_element3 = assertions.all_index_locator(contacts_page.list_elements())
    assert count_element3 == contact_count, (
        f"Ожидали количество элементов {contact_count}! Получили: {count_element3}")
    expect(contacts_page.static_page_locator()).to_have_text(contacts1)
