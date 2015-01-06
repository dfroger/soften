#!/usr/bin/env python

"""
Change hard links to symbolic links
"""

import os
import os.path as p
import argparse
import logging
from collections import defaultdict

def find_all_hardlinks(directory):
    all_hardlinks_dict = defaultdict(list)
    for root, dirs, files in os.walk(directory):
        for f in files:
            path = p.realpath(p.join(root,f))
            stat = os.stat(path)
            if stat.st_nlink > 1:
                all_hardlinks_dict[stat.st_ino].append(path)
    return [sorted(hardlinks) for hardlinks in all_hardlinks_dict.values()]

def soften_hardlinks(hardlinks,relative_path=False):
    source = hardlinks[0]
    for dest in hardlinks[1:]:
        os.remove(dest)
        logging.debug('rm %s' % (dest,))
        if relative_path:
            source = p.relpath(source, p.dirname(dest))
        os.symlink(source, dest)
        logging.debug('ln %s %s' % (source,dest))

def parse_command_line():
    parser = argparse.ArgumentParser(description='Change hard links to ' \
                                                 'symbolic links.')
    parser.add_argument('-v', '--verbose', action='store_true',
                        help='Print debug message')
    parser.add_argument('-t', '--log-to-file', metavar='FILENAME',
                        action='store',
                        help='Log debug messages to file instead of stdout')
    parser.add_argument('-d', '--relative-path', action='store_true',
                        help='Links to relative path instead of absolute.')
    parser.add_argument('root_directory', 
                        help='Root directory to search files recursively in.')
    args = parser.parse_args()
    return args

def configure_logging(args):
    conf = {}
    if args.verbose:
        conf['level'] = logging.DEBUG
    if args.log_to_file:
        conf['filename'] = args.log_to_file
    logging.basicConfig(**conf)

def main():
    args = parse_command_line()
    configure_logging(args)
    all_hardlinks = find_all_hardlinks(args.root_directory)
    for hardlinks in all_hardlinks:
        soften_hardlinks(hardlinks,args.relative_path)

if __name__ == '__main__':
    main()
