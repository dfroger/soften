soften
======

Change hard links to symbolic links

Usage:

    usage: soften.py [-h] [-v] [-t FILENAME] [-d] root_directory

    Change hard links to symbolic links.

    positional arguments:
      root_directory        Root directory to search files recursively in.

    optional arguments:
      -h, --help            show this help message and exit
      -v, --verbose         Print debug message
      -t FILENAME, --log-to-file FILENAME
                            Log debug messages to file instead of stdout
      -d, --relative-path   Links to relative path instead of absolute.

[Functional tests](tests/features/soften.feature) may also be a source of documentation.
