Feature: Admin login
    As a admin
    I want to write wrong login

Scenario: View Admin Panel
    Given I open the browser
    When I navigate to the admin panel
    And I enter wrong login and password
    Then I cant see the menu
    And I close the browser