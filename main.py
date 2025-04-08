import sys
from tree import Tree
import argparse
from routines import check_empty, check_has_epsilon

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_mutually_exclusive_group(required=True)
    parser.add_argument('--no-op', action='store_true')
    parser.add_argument('--simplify', action='store_true')
    parser.add_argument('--empty', action='store_true')
    parser.add_argument('--has-epsilon', action='store_true')
    parser.add_argument('--has-noepsilon', action='store_true')
    parser.add_argument('--uses')
    parser.add_argument('--not-using')
    parser.add_argument('--infinite', action='store_true')
    parser.add_argument('--starts-with')
    parser.add_argument('--reverse', action='store_true')
    parser.add_argument('--ends-with')
    parser.add_argument('--prefixes', action='store_true')
    parser.add_argument('--bs-for-a', action='store_true')
    parser.add_argument('--insert')
    parser.add_argument('--strip')
    return parser.parse_args()




def main():
    args = parse_args()

    for line in sys.stdin:
        if not line.strip():
            continue

        regx_tree = Tree()
        regx_tree.build_tree_from_postfix(line.strip())
        postfix_tree = regx_tree.get_pstfix_tree()

        try:
            if args.no_op:
                print(postfix_tree)
            elif args.simplify:
                pass
            elif args.empty:
                print('yes' if check_empty(postfix_tree) else 'no')
            elif args.has_epsilon:
                print('yes' if check_has_epsilon(postfix_tree) else 'no')
            elif args.has_nonepsilon:
                pass
            elif args.uses:
                pass
            elif args.not_using:
               pass
            elif args.infinite:
                pass
            elif args.starts_with:
                pass
            elif args.ends_with:
                pass
            elif args.reverse:
                pass
            elif args.prefixes:
                pass
            elif args.bs_for_a:
                pass
            elif args.insert:
                pass
            elif args.strip:
                pass
        except ValueError as e:
            sys.stderr.write(f"Error: {e}")

if __name__ == "__main__":
    main()