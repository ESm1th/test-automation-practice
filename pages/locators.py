from selenium.webdriver.common.by import By


class IndexPageLocators:
    PRODUCT_CARD = (By.CLASS_NAME, 'product-container')
    QUICK_LINK_BUTTON =  (
        By.XPATH,
        (
            '//div[@class="product-container"]/div[@class="left-block"]/'
            'div/a[@class="quick-view"]'
        )
    )
    QUICK_VIEW = (By.CLASS_NAME, 'fancybox-iframe')
    PRODUCT = (By.ID, 'product')


class QuickProductViewLocators:
    pass

