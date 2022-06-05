Feature: TESTS FOR AMAZON CART

  Scenario: Verify that NOT SIGNED-IN User is able to click on Cart and that Cart is empty
    Given Open Amazon page
    When Click on Cart
    Then Verify that Cart is empty

  Scenario: Verify that NOT SIGNED-IN User is able to add item into the Cart
    Given Open Amazon page
    When Search for toys
    Then Verify search results for "toys" are shown
    Then Scroll down
    And Click on any item
    Then Verify item is opened
    And Add item to the Cart
    Then Verify that item was added to the Cart
    When Click on Cart
    Then Verify that item is in the Cart
