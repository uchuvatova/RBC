from playwright.sync_api import Page, expect

#from tests.ui_tests.tests.conftest import page


def test_check_exit_button_visible(page: Page, main_page) -> None:
    main_page.goto()
    main_page.click_close_tv_popup_button()
    main_page.click_button_profile()
    expect(page.get_by_role("link", name="Вход")).to_be_visible()


def test_check_registration_button_visible(page: Page, main_page) -> None:
    main_page.goto()
    main_page.click_close_tv_popup_button()
    main_page.click_button_profile()
    expect(page.get_by_role("link", name="Регистрация")).to_be_visible()
