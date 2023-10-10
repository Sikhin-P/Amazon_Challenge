Feature: Amazon Challenge
  Scenario: Amazon Challenge
    Given Open a browser
    And Navigate to "https://www.amazon.in"
    When Search with "Camera"
    Then Verify and save search result