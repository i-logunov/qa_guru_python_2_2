import pytest
from selene.support.shared import browser
from selene import be, have

@pytest.fixture()
def set_browser_size():
    browser.config.window_width = 800
    browser.config.window_height = 600


def test_positive():
    browser.open('https://google.com/ncr')
    browser.element('[name="q"]').should(be.blank).type('selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))
    pass


def test_negative():
    browser.open('https://google.com/ncr')
    browser.element('[name="q"]').should(be.blank).type('2521ор1о1').press_enter()
    browser.element('[id="topstuff"]').should(have.text('Your search - 2521ор1о1 - did not match any documents'))
    pass