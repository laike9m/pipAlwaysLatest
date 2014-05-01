#TODO: other arguments should be directly passed to pip

import argparse
from subprocess import Popen, PIPE, check_output


def install(uv):
    import re
    try:
        with open("../requirements.txt", 'rt') as f:
            for package_line in f.readlines():
                if package_line.strip():  # blank lines don't count
                    obj = re.search(r'[\s>=<!]', package_line)
                    package = package_line[:obj.start()] if obj else package_line
                    if package.lower() not in uv:
                        print(check_output('pip install %s' % package).decode())
                    else:
                        print(check_output('pip install %s' % package_line).decode())
    except FileNotFoundError:
        print("No requirements.txt file!!")


def generate(uv):
    output = Popen("pip list", stdout=PIPE, stderr=PIPE)
    package_lines = output.stdout.readlines()
    packages = {line.decode().split()[0]: line.decode().split()[1] for line in package_lines}
    with open("requirements.txt", 'wt') as f:
        for package in packages:
            if package.lower() in uv:
                version = packages[package].strip('()')
                f.write(package + '==' + version + '\n')
            else:
                f.write(package + '\n')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='pip install/freeze latest version')
    parser.add_argument('method', metavar='method',
                        choices={'install', 'freeze'}, nargs=1,
                        help='method you want to apply, install/freeze')
    parser.add_argument('-v', '--version-packages', dest='use_version', nargs='+',
                        help='specify packages that will reserve version when generating \
                        requirements or install from requirements')

    args = parser.parse_args()
    print(args.method)
    print(args.use_version)
    use_version = [p.lower() for p in args.use_version] if args.use_version else []  # None->[]
    if args.method == ['install']:
        install(use_version)
    else:
        generate(use_version)
