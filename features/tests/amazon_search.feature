# Created by ivan at 2/3/24
Feature: Amazon search tests

  Scenario: User can search for table on Amazon
    Given Open amazon main page
    When Search for table
    Then Verify search results shown for "table"


  Scenario: User can search for coffee on Amazon
    Given Open amazon main page
    When Search for coffee
    Then Verify search results shown for "coffee"