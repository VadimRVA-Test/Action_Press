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
                        payment, title_payment)
from utils.hard_file import menu_news_count, menu_advantage_count, payment_count


class TestPaymentPage:
    def test_payment_page(self, action_page, payment_page, assertions):
        action_page.footer_control.click_footer_payment_button()
        assertions.all_locator(payment_page.collection_of_unique_locators())
        assertions.all_locator(payment_page.header_control.collection_of_unique_locators())
        expect(payment_page.header_control.header_locator()).to_have_attribute("data-qa-locator", header)
        expect(payment_page.menu_catalog.catalog_locator()).to_have_text(catalog)
        assertions.all_locator(payment_page.menu_catalog.collection_of_unique_locators())
        expect(payment_page.menu_catalog.catalog_locator()).to_have_text(catalog)
        assertions.all_locator(payment_page.menu_news.collection_of_unique_locators())
        count_elements = assertions.all_index_locator(payment_page.menu_news.collections_of_repeating_locators())
        assert (assertions.all_index_locator(payment_page.menu_news.collections_of_repeating_locators()) ==
                menu_news_count), f"Ожидали количество элементов {menu_news_count}! Получили: {count_elements}"
        expect(payment_page.menu_news.news_locator()).to_have_text(menu_news)
        expect(payment_page.menu_news.all_news_locator()).to_have_text(all_news)
        expect(payment_page.menu_advantages.advantages_locator()).to_have_text(menu_advantages)
        count_elements = assertions.all_index_locator(payment_page.menu_advantages.collections_of_repeating_locators())
        assert (assertions.all_index_locator(payment_page.menu_advantages.collections_of_repeating_locators()) ==
                menu_advantage_count), f"Ожидали количество элементов {menu_news_count}! Получили: {count_elements}"
        assertions.all_locator(payment_page.collection_of_unique_locators())
        count_elements = assertions.all_index_locator(payment_page.menu_advantages.collections_of_repeating_locators())
        assert (assertions.all_index_locator(payment_page.collections_of_repeating_locators()) ==
                payment_count), f"Ожидали количество элементов {payment_count}! Получили: {count_elements}"
        expect(payment_page.static_page_locator()).to_have_text(payment)
        expect(payment_page.non_cash_text_locator()).to_have_text(payment_non_cash)
        expect(payment_page.cash_text_locator()).to_have_text(payment_cash)
        expect(payment_page.card_text_locator()).to_have_text(payment_card)
        expect(payment_page.refound_text_locator()).to_have_text(payment_refound)

    def test_url_payment_page(self, action_page):
        action_page.footer_control.click_footer_payment_button()
        expect(action_page.page).to_have_title(title_payment)
        expect(action_page.page).to_have_url(PAYMENT_URL)
