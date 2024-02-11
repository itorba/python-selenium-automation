# Created by ivan at 2/11/24
Feature: Empty cart validation

  Scenario: User can see empty cart message
    Given Open target main page
    When Click on the cart icon
    Then Verify empty cart message shown
