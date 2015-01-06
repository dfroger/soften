#!/usr/bin/env python

"""
Change hard links to symbolic links
"""

import os
import os.path as p
import argparse
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
        if relative_path:
            source = p.relpath(source, p.dirname(dest))
        os.symlink(source, dest)

def main():
    parser = argparse.ArgumentParser(description='Change hard links to ' \
                                                 'symbolic links.')
    parser.add_argument('--relative-path', action='store_true',
                        help='Links to relative path instead of absolute.')
    parser.add_argument('file_or_dir', help='File or directory')
    args = parser.parse_args()

    all_hardlinks = find_all_hardlinks(args.file_or_dir)
    for hardlinks in all_hardlinks:
        soften_hardlinks(hardlinks,args.relative_path)

if __name__ == '__main__':
    main()
