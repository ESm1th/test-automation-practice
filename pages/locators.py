from selenium.webdriver.common.by import By


class IndexPageLocators:
    PRODUCT_CARD = (By.CLASS_NAME, 'product-container')
    QUICK_LINK_BUTTON = (
        By.XPATH,
        (
            '//div[@class="product-container"]/div[@class="left-block"]/'
            'div/a[@class="quick-view"]'
        )
    )
    QUICK_LINK_BUTTON_MOBIL = (
        By.XPATH,
        (
            '//div[@class="product-container"]/div[@class="left-block"]/'
            'div/div[@class="quick-view-wrapper-mobile"]/'
            'a[@class="quick-view-mobile"]'
        )
    )
    QUICK_VIEW = (By.CLASS_NAME, 'fancybox-iframe')
    PRODUCT = (By.ID, 'product')
    SHOPPING_CART = (By.XPATH, '//div[@class="shopping_cart"]')
    SHOPPING_CART_QUANTITY = (
        By.XPATH,
        '//span[@class="ajax_cart_quantity unvisible"]'
    )
    SHOPPING_CART_EMPTY = (
        By.XPATH,
        '//span[@class="ajax_cart_no_product"]'
    )


class QuickProductViewLocators:
    pass
