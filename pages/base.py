from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.elements.base import BaseWebElement


class BasePage:

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.url)

    @property
    def locators(self):
        raise NotImplementedError

    @property
    def title(self):
        """Returns web page title."""
        return self.browser.title

    @property
    def url(self):
        raise NotImplementedError

    def get_element(
        self, name: str, locator: tuple, element_type: BaseWebElement,
        timeout: int = 10
    ) -> BaseWebElement:
        """
        Waits for a specific element to be visible and returns specific class
        with this element in its initializer.
        """
        if name not in self.elements:
            element = self.browser.find_element(*locator)
            if not element.is_displayed():
                WebDriverWait(self.browser, timeout).until(
                    EC.visibility_of_element_located(locator)
                )
            self.elements[element] = element_type(element)
        return self.elements[element]
