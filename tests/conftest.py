import logging

import pytest
from pytest_bdd import given
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        '--browser_name', action='store', default='firefox',
        help='Choose browser: chrome or firefox.'
    )


@pytest.fixture
def available_browsers():
    browsers = {
        'firefox': webdriver.Firefox,
        'chrome': webdriver.Chrome
    }
    return browsers


@pytest.fixture
def get_driver(request, available_browsers):
    try:
        name = request.config.getoption('browser_name')
        return available_browsers[name]
    except KeyError:
        pytest.exit('Skipping all tests -> invalid browser name entered.')


@given('browser with window size "<width>", "<height>"')
def browser(get_driver, width, height):
    driver = get_driver()
    driver.set_window_size(width, height)
    yield driver
    driver.quit()
