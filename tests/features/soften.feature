Feature: Replace hard link with soft link

    Scenario: Replace three hard links with absolute path
        Given I create the following hardlinked files:
            | file |
            | foo  |
            | foo0 |
            | foo1 |
        When I run 'soften .'
        Then the following files are softlinked to the absolute path of 'foo':
            | file |
            | foo0 |
            | foo1 |

    Scenario: Replace three hard links with relative path
        Given I create the following hardlinked files:
            | file |
            | foo  |
            | foo0 |
            | foo1 |
        When I run 'soften --relative-path .'
        Then the following files are softlinked to 'foo':
            | file |
            | foo0 |
            | foo1 |

    Scenario: Replace nested hard links with absolute path
        Given I create the following hardlinked files:
            | file                  |
            | bin/foo               |
            | bin/foo0              |
            | libexec/foo-core/foo1 |
            | libexec/foo-core/foo2 |
        When I run 'soften .'
        Then the following files are softlinked to the absolute path of 'bin/foo':
            | file |
            | bin/foo0              |
            | libexec/foo-core/foo1 |
            | libexec/foo-core/foo2 |

    Scenario: Replace nested hard links with relative path
        Given I create the following hardlinked files:
            | file |
            | bin/foo               |
            | bin/foo0              |
            | libexec/foo-core/foo1 |
            | libexec/foo-core/foo2 |
        When I run 'soften --relative-path .'
        Then the following files are softlinked to 'foo':
            | file     |
            | bin/foo0 |
        Then the following files are softlinked to '../../bin/foo':
            | file                  |
            | libexec/foo-core/foo1 |
            | libexec/foo-core/foo2 |
