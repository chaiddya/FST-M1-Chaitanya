@activity4
  Feature: Data driven test without example

    Scenario: Testing with correct data from Scenario
      Given User is on Login page
      When user enters "admin" and "password"
      Then Read the page title and confirmation page
      Then close the browser


