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
    QUICK_VIEW = (
        By.XPATH,
        '//body[@id="product"]/div/div[@class="primary_block"]'
    )
