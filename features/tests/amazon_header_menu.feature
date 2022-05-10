Feature: TESTS FOR AMAZON HEADER MENU

  Scenario: Verify amount of sub-links under "Best Sellers" tab
    Given Open Amazon page
    When Verify Amazon page is opened
    And Click on Best Sellers
    Then Verify there are 5 sub-links under Best Sellers tab


  Scenario: Verify "Best Sellers" tab
    Given Open Amazon page
    When Verify Amazon page is opened
    And Click on Best Sellers
    Then Verify that Best Sellers page is opened
    When Click on New Releases page
    Then Verify that Amazon Hot New Releases page is opened
    When Click on Movers & Shakers page
    Then Verify that Amazon Movers & Shakers page is opened
    When Click on Most Wished For page
    Then Verify that Amazon Most Wished For page is opened
    When Click on Gift Ideas page
    Then Verify that Amazon Gift Ideas page is opened