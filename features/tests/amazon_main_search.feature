Feature: TESTS FOR AMAZON SEARCH FROM MAIN PAGE

  Scenario Outline: Verify that User can search for products
    Given Open Amazon page
    When Search for <search_word>
    Then Verify search results for <search_result> are shown
    Examples:
    |search_word   |search_result |
    |table         | "table"      |
    |dress         | "dress"      |
    |toys          | "toys"       |


#  Scenario: Verify that user can see product names and images
#    Given Open Amazon page
#    When Search for coffee
#    Then Verify that every product has a name and an image

