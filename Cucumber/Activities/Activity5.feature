@activity5
  Feature: Data driven test with example

    Scenario Outline: Testing wit data from Scenario
      Given User is on Login page
      When user enters "<Usernames>" and "<Password>"
      Then Read the page title and confirmation page

      Examples:
      | Usernames | Password |
      | admin     | password |
      |admin1     |password1 |
