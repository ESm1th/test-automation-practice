Feature: Adding product to shopping cart from product card
    
    As a client,
    I want to add product to product cart by clicking the button 
    on product card when monitoring product list on index page
    
    Scenario Outline: Add one product to shopping cart
        Given browser with window size "<width>", "<height>"
        And index page loaded
        And shopping cart is empty
        When user navigates to product card
        And clicks on button `add to cart`
        Then product added to shopping cart
        And quantity in shopping cart changed to 1
        
        Examples:
        |width|height|
        |1920|1080|
        |800|600|
    
    Scenario Outline: Adding several products to shopping cart
        Given browser with window size "<width>", "<height>"
        And index page loaded
        And shopping cart is empty
        When user navigates to one product card
        And clicks on button `add to cart`
        And user navigates to another product card
        And clicks on button `add to cart`
        Then products added to shopping cart
        And quantity in shopping cart changed to 2

        Examples:
        |width|height|
        |1920|1080|
        |800|600|
    