Feature: Message page
    As a user
    I want to see a non-empty title on the home page of the web application

Scenario: View home page with a non-empty title
    Given I open the browser
    When I navigate to the message page
    Then I should see a auth page
    And I close the browser