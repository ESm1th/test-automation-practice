import time

import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as cond


@pytest.fixture
def browser():
    driver_path = '/snap/bin/chromium.chromedriver'
    opts = Options()
    driver = Chrome(driver_path)
    yield driver
    driver.quit()


@pytest.fixture
def index_url():
    return 'http://automationpractice.com/'


def test_index_page(browser, index_url):
    browser.set_window_size(1920, 1080)
    browser.get(index_url)

    assert browser.title == 'My Store'

    product = browser.find_element_by_class_name('product-container')
    quick_view_link = product.find_element_by_xpath(
        './/div[@class="left-block"]/div/a[@class="quick-view"]'
    )

    # check that link `button` not displayed befor hover `product` element 
    assert quick_view_link.is_displayed() == False

    ActionChains(browser).move_to_element(product).perform()

    # check that link `button` is displayed after hover over `product` element
    assert quick_view_link.is_displayed() == True

    ActionChains(browser).move_to_element(quick_view_link).click().perform()
    time.sleep(4)


