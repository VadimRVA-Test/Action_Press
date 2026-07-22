from playwright.sync_api import expect
from utils.data import payment_non_cash, payment_cash, payment_card, payment_refound, payment, title_payment
from utils.hard_file import payment_count


class TestPaymentPage:
    def test_payment_page(self, action_page, payment_page, assertions):
        action_page.footer_control.click_footer_payment_button()
        assertions.assert_elements_count(payment_page.collections_of_repeating_locators(), payment_count, "payment")
        assertions.base_assertions(payment_page)
        expect(payment_page.static_page_locator()).to_have_text(payment)
        expect(payment_page.non_cash_text_locator()).to_have_text(payment_non_cash)
        expect(payment_page.cash_text_locator()).to_have_text(payment_cash)
        expect(payment_page.card_text_locator()).to_have_text(payment_card)
        expect(payment_page.refound_text_locator()).to_have_text(payment_refound)

    def test_url_payment_page(self, action_page, payment_page):
        action_page.footer_control.click_footer_payment_button()
        expect(action_page.page).to_have_title(title_payment)
        expect(action_page.page).to_have_url(action_page.composite_url(payment_page.PAYMENT_URL))
