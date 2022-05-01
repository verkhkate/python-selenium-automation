Feature: TESTS FOR AMAZON SEARCH FROM HELP PAGE

  Scenario: User can search for solutions of Canceling an order on Amazon from Help page
    When Open Amazon Help page
    When Verify Amazon Help page is opened
    Then Locate "Search Help Library" field and search for "Cancel order"
    Then Verify that "Cancel Items or Orders" text is displayed