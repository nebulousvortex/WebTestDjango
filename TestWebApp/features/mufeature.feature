Feature: Home Page Title
    As a user
    I want to see a non-empty title on the home page of the web application

Scenario: View home page with a non-empty title
    Given I open the browser
    When I navigate to the home page
    Then I should see a non-empty title
    And I close the browser