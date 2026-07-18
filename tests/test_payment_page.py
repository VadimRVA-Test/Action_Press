from playwright.sync_api import expect
from utils.data import (PAYMENT_URL,
                        header,
                        catalog,
                        menu_news,
                        all_news,
                        menu_advantages,
                        payment_non_cash,
                        payment_cash,
                        payment_card,
                        payment_refound,
                        payment)
from utils.hard_file import menu_news_count, menu_advantage_count, payment_count


def test_payment_page(action_page, payment_page, assertions):
    action_page.footer_control.footer_payment_button_locator().click()
    payment_page.page = action_page.page
    expect(payment_page.page).to_have_url(PAYMENT_URL)
    assertions.all_locator(payment_page.visible_elements())
    assertions.all_locator(payment_page.header_control.visible_elements())
    expect(payment_page.header_control.header_locator()).to_have_attribute("data-qa-locator", header)
    expect(payment_page.menu_catalog.catalog_locator()).to_have_text(catalog)
    assertions.all_locator(payment_page.menu_catalog.visible_elements())
    expect(payment_page.menu_catalog.catalog_locator()).to_have_text(catalog)
    assertions.all_locator(payment_page.menu_news.visible_elements())
    count_elements = assertions.all_index_locator(payment_page.menu_news.list_elements())
    assert assertions.all_index_locator(payment_page.menu_news.list_elements()) == menu_news_count, (
        f"Ожидали количество элементов {menu_news_count}! Получили: {count_elements}")
    expect(payment_page.menu_news.news_locator()).to_have_text(menu_news)
    expect(payment_page.menu_news.all_news_locator()).to_have_text(all_news)
    expect(payment_page.menu_advantages.advantages_locator()).to_have_text(menu_advantages)
    count_elements2 = assertions.all_index_locator(payment_page.menu_advantages.list_elements())
    assert assertions.all_index_locator(payment_page.menu_advantages.list_elements()) == menu_advantage_count, (
        f"Ожидали количество элементов {menu_news_count}! Получили: {count_elements2}")
    assertions.all_locator(payment_page.visible_elements())
    count_elements3 = assertions.all_index_locator(payment_page.menu_advantages.list_elements())
    assert assertions.all_index_locator(payment_page.list_elements()) == payment_count, (
        f"Ожидали количество элементов {payment_count}! Получили: {count_elements3}")
    expect(payment_page.static_page_locator()).to_have_text(payment)
    expect(payment_page.non_cash_text_locator()).to_have_text(payment_non_cash)
    expect(payment_page.cash_text_locator()).to_have_text(payment_cash)
    expect(payment_page.card_text_locator()).to_have_text(payment_card)
    expect(payment_page.refound_text_locator()).to_have_text(payment_refound)
