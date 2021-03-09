import os
import sys


def main():
    sys.argv.append("")  # 防止索引越界
    filename = sys.argv[1]
    if not os.path.isfile(filename):
        raise SystemExit(filename, ' does not exists')
    # Use the real uid/gid to test for access to a path.
    elif not os.access(filename, os.R_OK):
        raise SystemExit(filename, ' is not accessible')
    else:
        print(filename, ' is accessible')


if __name__ == '__main__':
    main()
