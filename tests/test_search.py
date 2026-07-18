from playwright.sync_api import expect
from utils.data import search_query, URl, No_products_found


def test_search(action_page):
    action_page.open_page()
    expect(action_page.page).to_have_url(URl)
    action_page.header_control.search_locator().click()
    action_page.header_control.search(search_query)
    expect(action_page.header_control.search2_locator()).to_have_value(search_query)
    action_page.header_control.search_button_locator().click()
    expect(action_page.header_control.result_locator()).to_contain_text(No_products_found)
