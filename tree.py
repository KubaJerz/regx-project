import sys

class Node:
    """Basic binary node for our parse tree"""
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        """prints out the tree in prefix notation"""
        if self.data is None:
            return ''
        elif self.left is None and self.right is None:
            return self.data
        elif self.right is None:  #  unary ops
            return f"{self.data}{str(self.left)}"
        else:  #  binary ops 
            return f"{self.data}{str(self.left)}{str(self.right)}"


class Tree:
    def __init__(self):
        self.head = None
        digits = {str(i) for i in range(10)}
        self.alphabet = (digits.union({chr(i) for i in range(ord('a'), ord('z')+1)})).union('/')
        self.unary = set(["*"])
        self.binary = set(["+", "."])

        
    def build_tree_from_postfix(self, expr):
        """Builds a parse tree from postfix notation"""
        stack = []
        for token in expr:
            if self.__isTerminal__(token):
                stack.append(Node(token))

            elif self.__isUnary__(token):
                left = stack.pop()
                stack.append(Node(token,left=left))

            elif self.__isBinary__(token):
                right = stack.pop()
                left = stack.pop()
                stack.append(Node(token,left=left, right=right))

            else:
                sys.stderr.write(f"ERROR: Parse Error when reading in expression: {expr} at token: {token}")

        self.head = stack[0]

    def get_pstfix_tree(self):
        """returns the head of the tree"""
        return self.head

    def __isTerminal__(self, a):
        """Chack is a is a terminal in our alphabet"""
        if a in self.alphabet:
            return True
        return False
    
    def __isUnary__(self, token):
        if token in self.unary:
            return True
        return False
    
    def __isBinary__(self, token):
        if token in self.binary:
            return True
        return False
    
    


