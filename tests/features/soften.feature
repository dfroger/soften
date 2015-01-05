Feature: Replace hard link with soft link
    Scenario: Manage three hard links 
        Given I create the following hardlinked files:
            | file |
            | bar  |
            | bar0 |
            | bar1 |
        When I run 'soften .'
        Then the following files are softlinked to 'bar':
            | file |
            | bar0 |
            | bar1 |
