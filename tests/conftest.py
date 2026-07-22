import pytest
from playwright.sync_api import sync_playwright
from pages.action_press_page import ActionPressPage
from pages.about_page import AboutPage
from pages.contacts_page import ContactsPage
from pages.payment_page import PaymentPage
from pages.auth_page import AuthPage
from utils.base_assertions import Assertions
from utils.credentials import credentials


@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as p:
        yield p


@pytest.fixture
def browser(playwright_instance):
    browser = playwright_instance.chromium.launch(headless=True, slow_mo=777)
    yield browser
    browser.close()


@pytest.fixture
def context(browser):
    context = browser.new_context()
    try:
        yield context
    finally:
        context.close()


@pytest.fixture
def page(context):
    page = context.new_page()
    page.set_viewport_size({"width": 1920, "height": 1080})
    return page


@pytest.fixture
def auth_page(page):
    return AuthPage(page)


@pytest.fixture
def auth_user_page(action_page, auth_page, context):
    action_page.open_page()
    with context.expect_page() as new_page:
        action_page.header_control.button_auth_reg_locator().click()
    auth_page.page = new_page.value
    auth_page.page.wait_for_timeout(3000)
    auth_page.authorize(credentials[0], credentials[1])
    action_page.open_page()
    return action_page


@pytest.fixture
def action_page(page):
    main_page = ActionPressPage(page)
    main_page.open_page()
    main_page.banner_control.click_accept_cookies()
    main_page.banner_control.click_close_jiva()
    return main_page


@pytest.fixture
def about_page(page):
    return AboutPage(page)


@pytest.fixture
def contacts_page(page):
    return ContactsPage(page)


@pytest.fixture
def payment_page(page):
    return PaymentPage(page)


@pytest.fixture
def assertions(page):
    return Assertions(page)
