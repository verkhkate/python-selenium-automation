Feature: Homework 8

#  Scenario: User can see language options
#    Given Open Amazon page
#    When Hover over language options
#    Then Verify Spanish option present


  Scenario Outline: User can select and search in a department
    Given Open Amazon page
    When Select department by <dept_alias>
    And Search for <search_query>
    Then Verify <selected_dept> department is selected
    Examples:
    |dept_alias           |search_query        |selected_dept      |
    |alexa-skills         |Apple               |digital-skills     |
    |amazon-devices       |Apple               |amazon-devices     |
    |amazonfresh          |Apple               |amazonfresh        |
    |tools                |axe handle          |hi                 |
    |pets                 |bowls for dogs      |pet-supplies       |


  Scenario: User can hover over New Arrivals in Clothing dept item and see the deals
    Given Open Amazon page
    When Select department by fashion
    And Search for hoodie
    Then Scroll down
    And Click on any item
    When Hover over New Arrivals
    Then Verify New Arrival deals are present
