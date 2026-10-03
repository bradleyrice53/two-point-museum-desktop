"""Two Point Museum Desktop — A local helper for Two Point Museum exhibit folders, staff notes, and gallery photos."""
from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='two_point_museum_desktop',
        description='A local helper for Two Point Museum exhibit folders, staff notes, and gallery photos.',
    )
    parser.add_argument('path', nargs='?', help='Input file or folder')
    parser.add_argument('--out', help='Output folder')
    parser.add_argument('--preview', help='Show the plan and do not write')
    args = parser.parse_args()
    print('Two Point Museum Desktop')
    print('Keep the museum on disk before a wing update.')
    print('Local CLI preview.')
    if vars(args):
        print(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
