import pytest
from selene import browser, be, have, by
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope='function', autouse=True)
def browser_setup():
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    yield
    browser.quit()


def test_google_search():
    browser.open('https://google.com/ncr')

    if browser.element(by.text('Принять все')).matching(be.visible):
        browser.element(by.text('Принять все')).click()

    search_box = browser.element('[name="q"]')
    search_box.should(be.blank).type('yashaka/selene').press_enter()

    search_results = browser.element('[id="search"]')
    search_results.should(have.text('User-oriented Web UI browser tests in Python'))


def test_google_search_no_results():
    browser.open('https://google.com/ncr')

    if browser.element(by.text('Принять все')).matching(be.visible):
        browser.element(by.text('Принять все')).click()

    search_box = browser.element('[name="q"]')
    search_box.should(be.blank).type('zxyqlv.ж;nwr;p23847hfglлаывав.ыавыацуцацxq').press_enter()

    search_results = browser.element('[id="search"]')
    search_results.should(have.text('did not match'))
