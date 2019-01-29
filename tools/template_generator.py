#!/usr/bin/env python3
import argparse
import os
import sys

try:
    import pyperclip as clipboard
except ImportError as e:
    print(e, '\nPlease install pyperclip module using PIP', file=sys.stderr)
    sys.exit(1)

COLORS = [f'{{{{ color{n} }}}}' for n in range(16)]


def get_cli_args():
    parser = argparse.ArgumentParser(
        description='Display color names in curly braces, copy output to clipboard')
    parser.add_argument('-p', '--pairs')
    parser.add_argument('-n', '--newlines', type=int, default=0, dest='newlines')
    args = parser.parse_args()
    return args


def norm_bright_pairs(newlines_between_pairs=0):
    for n, b in zip(COLORS[0:8], COLORS[8:16]):
        print(n)
        print(b)
        for nl in range(newlines_between_pairs):
            print()


if __name__ == '__main__':
    args = get_cli_args()
    norm_bright_pairs(args.newlines)
