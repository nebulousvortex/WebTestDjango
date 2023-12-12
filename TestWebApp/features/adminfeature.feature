Feature: Admin check
    As a admin
    I want to see a menu of admin page

Scenario: View Admin Panel
    Given I open the browser
    When I navigate to the admin panel
    And I enter my login and password
    Then I should see the menu
    And I close the browser