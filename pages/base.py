class BasePage:

    """
    Base page class. Common `__init__` method for all child classes.
    """

    def __init__(self, browser):
        self.browser = browser
    
    @property
    def url(self):
        raise NotImplementedError
    
    @property
    def locators(self):
        raise NotImplementedError
