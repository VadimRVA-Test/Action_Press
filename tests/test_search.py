from playwright.sync_api import expect
from utils.data import search_query, result_products


def test_search(action_page):
    action_page.header_control.search_locator().click()
    action_page.header_control.search(search_query)
    action_page.header_control.search_button_locator().click()
    expect(action_page.header_control.result_locator()).to_contain_text(result_products)
