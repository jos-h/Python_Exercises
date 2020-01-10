import argparse
import sys

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--x", type=float, default=1.0,
                        help="What is the first value?")

    parser.add_argument("--y", type=float, default=1.0,
                        help="What is the second value?")

    parser.add_argument("--op", type=str,
                        help="Which operations to perform? (add, sub, mul or div)")

    # parser.add_argument("square", type=int, help='display square of number')

    parser.add_argument("-v", "--verbose", action="store_true",
                        help="increase output verbosity")

    args = parser.parse_args()

    sys.stdout.write(str(calc(args)))


def calc(args):

    if args.op == 'add':
        return args.x + args.y
    if args.op == 'sub':
        return args.x - args.y
    if args.op == 'mul':
        return args.x * args.y
    if args.op == 'div':
        return args.x / args.y


if __name__ == '__main__':
    main()
