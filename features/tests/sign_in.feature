# Created by ivan at 2/11/24
Feature: Logged out user can sign in

  Scenario: Logged out user can access sign in page
    Given Open target main page
    When Click on the sign in
    When Click on the sign in from nav menu
    Then Verify sign in form shown