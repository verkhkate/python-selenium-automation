Feature: TESTS FOR AMAZON HELP PAGE

#  Scenario: User can search for solutions of Canceling an order on Amazon from Help page
#    When Open Amazon Help page
#    Then Verify Amazon Help page is opened
#    Then Locate "Search Help Library" field and search for "Cancel order"
#    Then Verify that "Cancel Items or Orders" text is displayed

  Scenario: Verify that Amazon Help page UI elements are present on the page

    Given Open Amazon page
    When Verify Amazon page is opened
    And Scroll down to the bottom menu
    When Open Amazon Help page
    Then Verify Amazon Help page is opened
    And Verify that Some things you can do here text result is displayed
    Then Verify that Your Orders text is displayed
    And Verify that Digital Services and Device Support text is displayed
    Then Verify that Your Account text is displayed
    And Verify that Returns & Refunds text is displayed
    Then Verify that Manage Prime text is displayed
    And Verify that Amazon and COVID-19 text is displayed
    Then Verify that Get Product Help text is displayed
    And Verify that Payments & Gift Cards text is displayed
    Then Verify that Safe Online Shopping text is displayed
    And Verify that Search the help library text is displayed
    Then Verify that "Type something like, question about a charge" text result is displayed
    Then Scroll down to "Browse Help Topics"
    And Verify that Browse Help Topics text is displayed
    Then Verifying that "Recommended Topics" text is displayed
    And Verify that Where is My Stuff text is properly displayed
    Then Verifying that "Shipping and Delivery" text is displayed
    And Verifying that "Returns and Refunds" text is displayed
    Then Verifying that "Managing Your Account" text is displayed
    And Verifying that "Security and Privacy" text is displayed
    Then Verifying that "Payment, Pricing & Promotions" text is displayed
    And Verifying that "Devices & Digital Services" text is displayed
    Then Verifying that "Amazon Business Accounts" text is displayed
    And Verifying that "Large Items and Heavy-Bulky Services" text is displayed
    Then Verifying that "Other Topics & Help Sites" text is displayed
    And Verifying that "Need More Help?" text is displayed
    Then Verify that "Wrenches icon" is displayed
