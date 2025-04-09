from tree import Node

digits = {str(i) for i in range(10)}
ALPHABET = digits.union({chr(i) for i in range(ord('a'), ord('z')+1)})
EMPTY_SET = '/' 

def check_empty(S):
    if S.data == EMPTY_SET:
        return True
    elif S.data in ALPHABET:
        return False
    elif S.data == '+':
        return check_empty(S.left) and check_empty(S.right)
    elif S.data == '.':
        return check_empty(S.left) or check_empty(S.right)
    elif S.data == '*':
        return False

def check_has_epsilon(S):
    if S.data == EMPTY_SET:
        return False
    elif S.data in ALPHABET:
        return False
    elif S.data == '+':
        return check_has_epsilon(S.left) or check_has_epsilon(S.right)
    elif S.data == '.':
        return check_has_epsilon(S.left) and check_has_epsilon(S.right)
    elif S.data == '*':
        return True
    
def check_has_nonepsilon(S):
    if S.data == EMPTY_SET:
        return False
    elif S.data in ALPHABET:
        return True
    elif S.data == '+':
        return check_has_nonepsilon(S.left) or check_has_nonepsilon(S.right)
    elif S.data == '.':
        return (check_has_nonepsilon(S.left) and not check_empty(S.right)) or (check_has_nonepsilon(S.right) and not check_empty(S.left))
    elif S.data == '*':
        return check_has_nonepsilon(S.left)
    
def check_uses_a(S, a):
    if S.data == EMPTY_SET:
        return False
    elif S.data in ALPHABET:
        return S.data == a
    elif S.data == '+':
        return check_uses_a(S.left, a) or check_uses_a(S.right, a)
    elif S.data == '.':
        return (check_uses_a(S.left, a) or check_uses_a(S.right, a)) and (not check_empty(S.left) and not check_empty(S.right))
    elif S.data == '*':
        return check_uses_a(S.left, a)
    
def check_is_infinite(S):
    if S.data == EMPTY_SET:
        return False
    elif S.data in ALPHABET:
        return False
    elif S.data == '+':
        return check_is_infinite(S.left) or check_is_infinite(S.right)
    elif S.data == '.':
        return (check_is_infinite(S.left) or check_is_infinite(S.right)) and (not check_empty(S.left) and not check_empty(S.right))
    elif S.data == '*':
        return check_has_nonepsilon(S)
    
def check_starts_with(S, a):
    if S.data == EMPTY_SET:
        return False
    elif S.data in ALPHABET:
        return S.data == a
    elif S.data == '+':
        return check_starts_with(S.left, a) or check_starts_with(S.right, a)
    elif S.data == '.':
        return (check_starts_with(S.left, a) or (check_has_epsilon(S.left) and check_starts_with(S.right, a))) and (not check_empty(S.left) and not check_empty(S.right))
    elif S.data == '*':
        return check_starts_with(S.left, a)
    
def check_ends_with(S, a):
    if S.data == EMPTY_SET:
        return False
    elif S.data in ALPHABET:
        return S.data == a
    elif S.data == '+':
        return check_ends_with(S.left, a) or check_ends_with(S.right, a)
    elif S.data == '.':
        return (check_ends_with(S.right, a) or (check_has_epsilon(S.right) and check_ends_with(S.left, a))) and (not check_empty(S.left) and not check_empty(S.right))
    elif S.data == '*':
        return check_ends_with(S.left, a)
    
def create_reverse(S):
    if S.data == EMPTY_SET:
        return S
    elif S.data in ALPHABET:
        return S
    elif S.data == '+':
        return Node(S.data, create_reverse(S.left), create_reverse(S.right))
    elif S.data == ".":
        return Node(S.data, create_reverse(S.right), create_reverse(S.left))
    elif S.data == "*":
        return Node(S.data, create_reverse(S.left))
    
def create_not_using(S, a):
    if S.data == EMPTY_SET:
        return S
    elif S.data in ALPHABET:
        if S.data == a:
            return Node(EMPTY_SET)
        else:
            return S
    elif S.data in set(['+', '.']):
        left = create_not_using(S.left, a)
        right = create_not_using(S.right, a)
        return Node(S.data, left, right)
    elif S.data == '*':
        return Node(S.data, create_not_using(S.left, a))
    
def create_prefixes(S):
    if S.data == EMPTY_SET:
        return S
    elif S.data in ALPHABET:
        empty_str = Node('*', left=Node(EMPTY_SET), right=None) #to make /*
        return Node('+', S, empty_str)
    elif S.data == "+":
        return Node(S.data, create_prefixes(S.left), create_prefixes(S.right))
    elif S.data == ".":
        if check_empty(S.right):
            return Node(EMPTY_SET)
        else:
            left = create_prefixes(S.left) # s'
            right = Node('.', S.left, create_prefixes(S.right)) # st'
            return Node('+', left, right)
    elif S.data == "*":
        if check_empty(S.left):
            return Node('*', left=Node(EMPTY_SET), right=None) #to make /*
        else:
            return Node('.', S, create_prefixes(S.left)) # s*s'
        
def create_bs_for_a(S):
    if S.data == EMPTY_SET:
        return S
    elif S.data in ALPHABET:
        if S.data == 'a':
            return Node('*', Node('b'))
        else:
            return S
    elif S.data == '+':
        return Node(S.data, create_bs_for_a(S.left), create_bs_for_a(S.right))
    elif S.data == '.':
        return Node(S.data, create_bs_for_a(S.left), create_bs_for_a(S.right))
    elif S.data == '*':
        return Node(S.data, create_bs_for_a(S.left))
    
def create_insert(S, a):
    if S.data == EMPTY_SET:
        return S
    elif S.data in ALPHABET:
        left = Node('.', Node(a), S.data)
        right = Node('.', S.data, Node(a))
        return Node('+', left, right)
    elif S.data == '+':
        return Node(S.data, create_insert(S.left, a), create_insert(S.right, a))
    elif S.data == '.':
        left_insert = Node('.', create_insert(S.left, a), S.right)
        right_insert = Node('.', S.left, create_insert(S.right, a))
        return Node('+', left_insert, right_insert)
    elif S.data == '*':
        pre = Node(a)
        
        double_star = Node('*', Node('*', S.left))  # a** for both sides
        
        if a == EMPTY_SET or S.left.data == EMPTY_SET: #if one is then the concat will be jsut the empty set
            innner = Node(EMPTY_SET)
        else:
            before_symbol = Node('.', Node(a), S.left)  # ba
            after_symbol = Node('.', S.left, Node(a))   # ab
            innner = Node('+', before_symbol, after_symbol)  # (ba+ab)
        
        combined = Node('.', Node('.', double_star, innner), double_star)
        
        return Node('+', pre, combined) 


def create_strip(S, a):
    if S.data == EMPTY_SET:
        return S
    elif S.data in ALPHABET:
        if S.data == a:
            return Node('*', Node(EMPTY_SET))
        else:
            return Node(EMPTY_SET)
    elif S.data == '+':
        return Node(S.data, create_strip(S.left, a), create_strip(S.right, a))
    elif S.data == '.':
        if check_has_epsilon(S.left):
            left = Node('.', create_strip(S.left, a), S.right)
            return Node('+', left, create_strip(S.right, a))
        else:
            return Node('.', create_strip(S.left, a), S.right)
    elif S.data == "*":
        return Node('.', create_strip(S.left, a), Node('*', S.left))

def simplify_until_fixed_point(S):
    """do the  simplify until does not change any more"""
    current = S
    while True:
        simplified = create_simplify(current)
        if str(simplified) == str(current):
            return simplified
        current = simplified
    
def create_simplify(S):
    if S is None:
        return None
        
    # recurse over the children
    if S.data in ['+', '.']:
        S.left = create_simplify(S.left)
        S.right = create_simplify(S.right)
    elif S.data == '*':
        S.left = create_simplify(S.left)
    
  
    # rule 1 s** -> s*
    if S.data == '*' and S.left and S.left.data == '*':
        return S.left
        
    #rules 2
    if S.data == '+':
        if S.left.data == EMPTY_SET:
            return S.right
        if S.right.data == EMPTY_SET:
            return S.left
            
    #rule 3
    if S.data == '.':
        if S.left.data == EMPTY_SET or S.right.data == EMPTY_SET:
            return Node(EMPTY_SET)
            
    #rule 4
    if S.data == '.':
        if S.left.data == '*' and S.left.left.data == EMPTY_SET:
            return S.right
        if S.right.data == '*' and S.right.left.data == EMPTY_SET:
            return S.left
            
    #rule 5
    if S.data == '*' and S.left.data == '+':
        if (S.left.left.data == '*' and S.left.left.left.data == EMPTY_SET):
            return Node('*', S.left.right)
        if (S.left.right.data == '*' and S.left.right.left.data == EMPTY_SET):
            return Node('*', S.left.left)
            
    return S