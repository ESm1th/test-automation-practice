from abc import ABC, abstractmethod
from selenium.webdriver.remote.webelement import WebElement


class BaseWebElement(ABC):

    def __init__(self, element: WebElement) -> None:
        self.__element = element

    def __getattr__(self, attr: str):
        if attr in self.__dict__:
            return getattr(self, attr)
        return getattr(self.__element, attr)

    @property
    def element(self):
        return self.__element

    @property
    @abstractmethod
    def locators(self):
        pass
