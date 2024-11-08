import pytest
from selene import browser, be, have, by
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope='function', autouse=True)
def browser_setup():
    options = webdriver.ChromeOptions()
    options.add_argument('--window-size=1200,800')
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    browser.set_driver(driver)
    yield
    browser.quit()

def test_google_search():
    browser.open_url('https://google.com')
    if browser.element(by.text('Принять все')).matching(be.visible):
        browser.element(by.text('Принять все')).click()

    search_box = browser.element('[name="q"]')
    search_box.should(be.blank).type('yashaka/selene').press_enter()

    search_results = browser.element('[id="search"]')
    search_results.should(have.text('User-oriented Web UI browser tests in Python'))
