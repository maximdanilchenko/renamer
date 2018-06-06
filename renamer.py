import os
import re
import shutil
import argparse
from pathlib import Path
from pprint import pprint


def rename(pattern_file, path_to, pattern_from, pattern_to, rec):
    os.makedirs(path_to, exist_ok=True)
    p = Path('.')
    fls = list(p.glob('**/%s' % pattern_file if rec else pattern_file))
    errors = {}
    for f in fls:
        try:
            shutil.copy(f, Path(path_to).joinpath(re.sub(pattern_from,
                                                         pattern_to,
                                                         f.name)))
        except Exception as e:
            errors[f.as_posix()] = e.__str__()
    if errors:
        print('Errors:')
        pprint(errors)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Copy files with renaming by pattern')
    parser.add_argument('pattern_file', help='pattern for files to search')
    parser.add_argument('path_to', help='path where to save result files')
    parser.add_argument('pattern_from',
                        help='regex for file name to find substrings')
    parser.add_argument('pattern_to',
                        help='replacing string with backreferences '
                             'from regex pattern_from argument')
    parser.add_argument('--r', dest='rec', default=False,
                        const=True, action='store_const',
                        help='find recursively in all subdirectories')
    args = parser.parse_args()
    rename(
        args.pattern_file,
        args.path_to,
        args.pattern_from,
        args.pattern_to,
        args.rec
    )
