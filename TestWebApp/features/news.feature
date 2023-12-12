Feature: news check
    As a admin
    I want to see all news

Scenario: View News Panel
    Given I open the browser
    When I navigate to news panel
    Then I should see the news
    And I close the browser