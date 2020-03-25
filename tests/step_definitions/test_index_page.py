import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from selenium.webdriver import Chrome
# from selenium.webdriver.chrome.options import Options

from pages.index import IndexPage


scenarios('../features/index_page/show_quick_view.feature')
scenarios('../features/index_page/add_to_cart_from_card.feature')


EXTRA_TYPES = {'Number': int}
CONVERTERS = {'width': int, 'height': int}


@given('browser with window size "<width>", "<height>"')
def browser(width, height):
    driver_path = '/snap/bin/chromium.chromedriver'
    driver = Chrome(driver_path)
    driver.set_window_size(width, height)
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def index_page(browser):
    index_page = IndexPage(browser)
    return index_page


@given('index page loaded')
def load_index_page(index_page):
    index_page.load()


@when('the user moves mouse to the product card')
def move_to_product_card(index_page):
    index_page.show_quick_view_button()


@when('the user clicks on displayed quick view button link')
def show_quick_view(index_page):
    index_page.show_quick_view()


@when('the user move mouse to eye icon on product card and click on it')
def show_quick_view_mobil(index_page):
    index_page.show_quick_view(mobil=True)


@then('quick view is displayed')
def quick_view_is_displayed(index_page):
    assert index_page.get_quick_view().is_displayed()
