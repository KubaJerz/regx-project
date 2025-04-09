import sys
from tree import Tree
import argparse
from routines import check_empty, check_has_epsilon, check_has_nonepsilon, check_uses_a, create_not_using, check_is_infinite, check_starts_with, check_ends_with, create_reverse, create_prefixes, create_bs_for_a, create_insert, create_strip, create_simplify, simplify_until_fixed_point

def parse_args():
    parser = argparse.ArgumentParser()
    # parser.add_mutually_exclusive_group(required=True)
    parser.add_argument('--no-op', action='store_true')
    parser.add_argument('--simplify', action='store_true')
    parser.add_argument('--empty', action='store_true')
    parser.add_argument('--has-epsilon', action='store_true')
    parser.add_argument('--has-nonepsilon', action='store_true')
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
                print(simplify_until_fixed_point(postfix_tree))
            elif args.empty:
                print('yes' if check_empty(postfix_tree) else 'no')
            elif args.has_epsilon:
                print('yes' if check_has_epsilon(postfix_tree) else 'no')
            elif args.has_nonepsilon:
                print('yes' if check_has_nonepsilon(postfix_tree) else 'no')
            elif args.uses:
                print('yes' if check_uses_a(postfix_tree, args.uses) else 'no')
            elif args.not_using:
               print(create_not_using(postfix_tree, args.not_using))
            elif args.infinite:
                print('yes' if check_is_infinite(postfix_tree) else 'no')
            elif args.starts_with:
                print('yes' if check_starts_with(postfix_tree, args.starts_with) else 'no')
            elif args.ends_with:
                print('yes' if check_ends_with(postfix_tree, args.ends_with) else 'no')
            elif args.reverse:
                print(create_reverse(postfix_tree))
            elif args.prefixes:
                print(create_prefixes(postfix_tree))
            elif args.bs_for_a:
                print(create_bs_for_a(postfix_tree))
            elif args.insert:
                print(create_insert(postfix_tree, args.insert))
            elif args.strip:
                print(create_strip(postfix_tree, args.strip))
        except ValueError as e:
            sys.stderr.write(f"Error: {e}")

if __name__ == "__main__":
    main()