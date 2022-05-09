#!python3

from prefixtreenode import PrefixTreeNode


class PrefixTree:
    """PrefixTree: A multi-way prefix tree that stores strings with efficient
    methods to insert a string into the tree, check if it contains a matching
    string, and retrieve all strings that start with a given prefix string.
    Time complexity of these methods depends only on the number of strings
    retrieved and their maximum length (size and height of subtree searched),
    but is independent of the number of strings stored in the prefix tree, as
    its height depends only on the length of the longest string stored in it.
    This makes a prefix tree effective for spell-checking and autocompletion.
    Each string is stored as a sequence of characters along a path from the
    tree's root node to a terminal node that marks the end of the string."""

    # Constant for the start character stored in the prefix tree's root node
    START_CHARACTER = ''

    def __init__(self, strings=None):
        """Initialize this prefix tree and insert the given strings, if any."""
        # Create a new root node with the start character
        self.root = PrefixTreeNode(PrefixTree.START_CHARACTER)
        # Count the number of strings inserted into the tree
        self.size = 0
        # Insert each string, if any were given
        if strings is not None:
            for string in strings:
                self.insert(string)

    def __repr__(self):
        """Return a string representation of this prefix tree."""
        return f'PrefixTree({self.strings()!r})'

    def is_empty(self):
        """Return True if this prefix tree is empty (contains no strings)."""
        if not self.size:
             return True
        return False

    def contains(self, string):
        """Return True if this prefix tree contains the given string."""
        p = self.root
        
        for letter in string:
            if letter not in p.children:
                return False
            p = p.children[letter]

        if p.terminal:
            return True
        else:
            return False
        

    def insert(self, string):
        """Insert the given string into this prefix tree."""
        p = self.root
        new = False
        
        for letter in string:
            if letter not in p.children:
                p.children[letter] = PrefixTreeNode(letter)
                new = True
            p = p.children[letter]

        p.terminal = True

        if new:
            self.size += 1
        

    def _find_node(self, string):
        """Return a pair containing the deepest node in this prefix tree that
        matches the longest prefix of the given string and the node's depth.
        The depth returned is equal to the number of prefix characters matched.
        Search is done iteratively with a loop starting from the root node."""
        # Match the empty string
        if len(string) == 0:
            return self.root, 0
        # Start with the root node
        node = self.root

        for c in string:
            if c not in node.children:
                return None, 0
            node = node.children[c]
        return node, len(string)
        

    def complete(self, prefix):
        """Return a list of all strings stored in this prefix tree that start
        with the given prefix string."""
        # Create a list of completions in prefix tree
        completions = []
        current = self.root

        for c in prefix:
            if c not in current.children:
                return []

            current = current.children[c]

            if current is None:
                return []

        self._traverse(current, prefix, completions)

        return completions
        

    def strings(self):
        """Return a list of all strings stored in this prefix tree."""
        # Create a list of all strings in prefix tree
        all_strings = []
        self._traverse(self.root, '', all_strings)
        return all_strings

    def _traverse(self, node, prefix, visit):
        """Traverse this prefix tree with recursive depth-first traversal.
        Start at the given node with the given prefix representing its path in
        this prefix tree and visit each node with the given visit function."""
        if node.terminal == True:
            visit.append(prefix)
        for a, n in node.children.items():
            self._traverse(n, prefix + a, visit)
