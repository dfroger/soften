#!/usr/bin/env python

"""
Change hard links to symbolic links
"""

import os
import argparse
from collections import defaultdict

def find_all_hardlinks(directory):

    all_hardlinks_dict = defaultdict(list)

    for root, dirs, files in os.walk(directory):
        for f in files:
            path = os.path.join(root,f)
            stat = os.stat(path)
            if stat.st_nlink > 1:
                all_hardlinks_dict[stat.st_ino].append(path)

    return [sorted(hardlinks) for hardlinks in all_hardlinks_dict.values()]

def soften_hardlinks(hardlinks):
    source = hardlinks[0]
    for path in hardlinks[1:]:
        os.remove(path)
        os.symlink(source, path)

def main():
    parser = argparse.ArgumentParser(description='Change hard links to ' \
                                                 'symbolic links.')
    parser.add_argument('file_or_dir', help='File or directory')
    args = parser.parse_args()

    all_hardlinks = find_all_hardlinks(args.file_or_dir)
    for hardlinks in all_hardlinks:
        soften_hardlinks(hardlinks)

if __name__ == '__main__':
    main()
