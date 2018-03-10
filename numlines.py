#!/usr/bin/env python

"""
This script will iteratively scan a directory and each sub directory, reading
each file, and counting the total number of lines.

This script will ignore any empty lines, and other directory that should not
be scanned such as dotfiles and dotdirectories (.node_modules, .git) and
build/, etc.
"""

import os

queue = []
def get_dir_content(path):
    entries = os.listdir(path)

# Handle command line arguments
# By default display totals lines, else if verbose then more information

def main():
    paths_scanned = []
    entries = os.listdir(path)
    for entry in entries:
        while os.path.isdir(entry):
            entry = os.listdir(path)


if __name__ == "__main__":
    main()
