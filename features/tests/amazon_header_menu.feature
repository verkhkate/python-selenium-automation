Feature: TESTS FOR AMAZON HEADER MENU

  Scenario: Verify "Best Sellers"
    Given Open Amazon page
    When Verify Amazon page is opened
    And Click on "Best Sellers"
    Then Verify that "Best Sellers" page is opened
    When Click on "New Releases"
    Then Verify that "New Releases" page is opened
    When Click on "Movers & Shakers"
    Then Verify that "Movers & Shakers" page is opened
    When Click on "Most Wished For"
    Then Verify that "Most Wished For" page is opened
    When Click on "Gift Ideas"
    Then Verify that "Gift Ideas" page is opened