Feature: Login test

  @allure.label.test:testing
  Scenario: User can open and log into Reelly
    Given Open login page
    When Login into Reelly
    Then Verify menu landing page
    When User select settings
    Then Verify settings page
    When User clicks edit profile
    Then Verify profile page is displayed
    When User updates company text
    Then Verify Company's text is updated
    When User selects save changes
    When User selects close
    Then Verify settings page
    When User clicks edit profile
    Then Verify profile page is displayed
    Then Verify Company's text is updated
    When User clears company text
    And User selects save changes