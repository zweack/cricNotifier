import argparse


def parse_arguments():
    parser = argparse.ArgumentParser(description="cricNotifier")
    parser.add_argument('-t', '--timeout',
                        help='duration of system notification')
    parser.add_argument('-i', '--interval',
                        help='duration between each notification')
    parser.add_argument('-nl', '--nologs',
                        action='store_true',
                        help='disable console logs',
                        default=False
                        )
    args = parser.parse_args()
    return args, parser
