

Feature: Testing the main page functionality

  Scenario: Verify product status on the off-plan page
    Given I open the main page "url"
    When I log in to the page
    And click the continue button
    And I click on "off plan" at the left side menu
    Then I verify the right page opens
    When I filter by sale status of "Out of Stock"
   Then I verify each product contains the "Out of Stock" tag

