Feature: Replace hard link with soft link

    Scenario: Replace three hard links with absolute path
        Given I create the following hardlinked files:
            | file |
            | bar  |
            | bar0 |
            | bar1 |
        When I run 'soften .'
        Then the following files are softlinked to the absolute path of 'bar':
            | file |
            | bar0 |
            | bar1 |

    Scenario: Replace three hard links with relative path
        Given I create the following hardlinked files:
            | file |
            | bar  |
            | bar0 |
            | bar1 |
        When I run 'soften --relative-path .'
        Then the following files are softlinked to 'bar':
            | file |
            | bar0 |
            | bar1 |
