from playwright.sync_api import expect


def test_payment_page(payment_page):
    payment_page.open_page(payment_page.PAYMENT_URL)
    expect(payment_page.page).to_have_url("https://action-press.ru/about/payment/")
    for locator in payment_page.visible_elements():
        expect(locator).to_be_visible()
