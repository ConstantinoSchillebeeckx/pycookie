#!/usr/bin/env python3
'''
Docs

Usage
-----

>>> ./main.py

'''

import argparse
from prog import something


def main(args):
    '''
    '''

    something.some_func()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        usage=__doc__,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser._action_groups.pop()
    required = parser.add_argument_group('required arguments')
    optional = parser.add_argument_group('optional arguments')

    required.add_argument(
        "-i",
        "--input",
        required=True,
        help=(
            "input file"
        )
    )

    optional.add_argument(
        "-o",
        "--output",
        default=None,
        help=(
            "output file"
        )
    )

    args = parser.parse_args()
    main(args)
