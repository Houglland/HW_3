from selene import browser, be, have, by

browser.open_url('https://google.com')
if browser.element(by.text('Принять все')).matching(be.visible):
    browser.element(by.text('Принять все')).click()
browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
browser.element('[id="search"]').should(have.text('User-oriented Web UI browser tests in Python'))
