Feature: add new text to news

    @success
    Scenario Outline: Запись может быть добавлена
        Given I open the browser
        When I navigate to login page
        And I enter admin login <log> and password <pass>
        Examples:
            | log    | pass  |
            | vortex | spaceofvortex11 |
            | vortex2| W9y-c2g-yZD-mGx |
        Then I navigate to add news panel
        And I try to add new news <title> <anons> <full_text>
        Examples:
            | title    | anons  | full_text |
            | test1 | test new | 1 try to add new news|
            | test2 | test new | 2 try to add new news|
            | test3 | test new | 3 try to add new news|
            | test4 | test new | 4 try to add new news|
        And I close the browser

        @fail
    Scenario Outline: Добавить запись не удалось
        Given I open the browser
        When I navigate to login page
        And I enter admin login <log> and password <pass>
        Examples:
            | log    | pass  |
            | vortex | spaceofvortex11 |
            | vortex2| W9y-c2g-yZD-mGx |
        Then I navigate to add news panel
        And I try to add new news <title> <anons> <full_text>
        Examples:
            | title    | anons  | full_text |
            | | test new | 1 try to add new news|
            | test2 | | 2 try to add new news|
            | test3 | test new | |
        And I close the browser