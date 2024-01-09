Feature: Admin login with
    As a admin
    I want to write wrong login

    @success
    Scenario Outline: Вход в панель админа успешен
        Given I open the browser
        When I navigate to the admin panel
        And I enter my login <log> and password <pass>
        Examples:
            | log    | pass  |
            | vortex | spaceofvortex11 |
            | vortex2| W9y-c2g-yZD-mGx |
        Then I should see the menu
        And I close the browser

    @fail
    Scenario Outline: Вход был неудачен
        Given I open the browser
        When I navigate to the admin panel
        And I enter wrong login <log> or password <pass>
        Examples:
            | log  | pass  |
            | vrtx | ggggg |
            | vorx | ppppp |
            | vote | vvvvv |
            | testLog | testPas |
        Then I cant see the menu
        And I close the browser