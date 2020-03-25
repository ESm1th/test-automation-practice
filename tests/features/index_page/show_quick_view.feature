Feature: Quick product view

   As a client,
   I want to hover over product card or click on it on web page
   and get quick view of this product.

   Scenario Outline: Hover over (wide window size)
      Given browser with window size "<width>", "<height>"
      And index page loaded
      When the user moves mouse to the product card
      And the user clicks on displayed quick view button link
      Then quick view is displayed

      Examples:
      |width|height|
      |1920|1080|

   Scenario Outline: Click on product card
      Given browser with window size "<width>", "<height>"
      And index page loaded
      When the user move mouse to eye icon on product card and click on it
      Then quick view is displayed

      Examples:
      |width|height|
      |800|600|