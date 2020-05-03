import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        '--browser', action='store', default='firefox',
        help='Choose browser: chrome or firefox.'
    )


@pytest.fixture(scope='session')
def available_browsers():
    browsers = {
        'firefox': webdriver.Firefox,
        'chrome': webdriver.Chrome
    }
    return browsers


@pytest.fixture(scope='session')
def get_driver(request, available_browsers):
    try:
        name = request.config.getoption('browser')
        return available_browsers[name]
    except KeyError:
        pytest.exit('Skipping all tests -> invalid browser name entered.')


@pytest.fixture
def browser(get_driver):
    driver = get_driver()
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()
