#!/usr/bin/env python3
import argparse
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
    parser.add_argument('-p', '--pairs', action='store_true')
    parser.add_argument('-n', '--newlines', type=int, default=0, dest='newlines')
    return parser.parse_args()


def list_color_pairs(newlines=0):
    result = ''
    for neutral, bright in zip(COLORS[0:8], COLORS[8:16]):
        result += f'{neutral}\n{bright}\n' + '\n' * newlines
    return result.strip()


def list_colors(newlines_between_pairs=0):
    result = ''
    for color in COLORS:
        result += color + '\n'
    return result.strip()


if __name__ == '__main__':
    args = get_cli_args()
    if args.pairs:
        output = list_color_pairs(args.newlines)
    else:
        output = list_colors(args.newlines)
    clipboard.copy(output)
    print(output)
