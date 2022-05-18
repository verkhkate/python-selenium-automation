Feature: TESTS FOR AMAZON SEARCH FROM MAIN PAGE

#  Scenario Outline: Verify that User can search for products
#    Given Open Amazon page
#    When Search for <search_word>
#    Then Verify search results for <search_result> are shown
#    Examples:
#    |search_word   |search_result |
#    |table         | "table"      |
#    |dress         | "dress"      |
#    |toys          | "toys"       |

  Scenario: Verify that every product on Amazon search results page has product name and image
    Given Open Amazon page
    When Search for mens jeans
    Then Scroll to the bottom of search results
    Then Verify that every product on Amazon search results page has product name and image
