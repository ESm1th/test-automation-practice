import time

import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options

from pages.index import IndexPage


@pytest.fixture
def browser():
    driver_path = '/snap/bin/chromium.chromedriver'
    driver = Chrome(driver_path)
    driver.set_window_size(1920, 1080) 
    yield driver
    driver.quit()


def test_index_page_load_product_quick_view(browser):
    """
    Test case:
        - load `index` page
        - check one product card and that `quick view` button link
        not displayed on it
        - move mouse on product card
        - check that `quick view` button link is displayed now
        - click on `quick view` button link and verify that `quick view` iframe
        loaded and displayed
    """
    index_page = IndexPage(browser)
    index_page.load()

    # check title of `index` page
    assert index_page.title == 'My Store'

    # check that link `button` not displayed befor hover `product` element 
    assert index_page.quick_view_button.is_displayed() == False

    # check that link `button` is displayed after hover over `product` element
    index_page.show_quick_view_button()
    assert index_page.quick_view_button.is_displayed() == True

    # check that `iframe` loaded and displayed
    index_page.show_quick_view()
    assert index_page.quick_view.is_displayed() == True