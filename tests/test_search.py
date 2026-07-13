from playwright.sync_api import expect


def test_search(action_page):
    search_query = 'Электронный журнал. ВИП-версия "Главбух" 12 мес.'
    action_page.open_page()
    action_page.close_button.accept_cookies_button_locator().click()
    action_page.close_button.close_jiva_button_locator().click()
    action_page.header_control.search_locator().click()
    action_page.header_control.search(search_query)
    expect(action_page.header_control.search2_locator()).to_have_value(search_query)
    action_page.header_control.search_button_locator().click()
    expect(action_page.header_control.result_locator()).to_contain_text("Товаров не найдено")
