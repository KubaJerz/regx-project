from routine_utils import is_emptyset, is_terminal, is_kleene, is_union, is_concat

def is_empty(S):
    if is_emptyset(S.head):
        return True
    elif is_terminal(S.head):
        return False
    elif is_kleene(S.head):
        return False
    elif is_union(S.head):
        return is_empty(S.left) and is_empty(S.right)
    elif is_concat(S.head):
        return is_empty(S.left) and is_empty(S.right)