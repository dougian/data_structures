from collections import defaultdict

class Trie:
    def __init__(self):
        self.root = defaultdict(Trie)
        self.value = None

    def add(self, s, value):
        """Add the string `s` to the
        `Trie` and map it to the given value."""
        head, tail = s[0], s[1:]
        cur_node = self.root[head]
        if not tail:
            cur_node.value = value
            return  # No further recursion
        self.root[head].add(tail, value)

    def lookup(self, s, default=None):
        """Look up the value corresponding to
        the string `s`. Expand the trie to cache the search."""
        head, tail = s[0], s[1:]
        node = self.root[head]
        if tail:
            return node.lookup(tail)
        return node.value or default

    def remove(self, s):
        """Remove the string s from the Trie.
        Returns *True* if the string was a member."""
        head, tail = s[0], s[1:]
        if head not in self.root:
            return False  # Not contained
        node = self.root[head]
        if tail:
            return node.remove(tail)
        else:
            del node
            return True

    def prefix(self, s):
        """Check whether the string `s` is a prefix
        of some member. Don't expand the trie on negatives (cf.lookup)"""
        if not s:
            return True
        head, tail = s[0], s[1:]
        if head not in self.root:
            return False  # Not contained
        node = self.root[head]
        return node.prefix(tail)

    def items(self):
        """Return an iterator over the items of the `Trie`."""
        for char, node in self.root.iteritems():
            if node.value is None:
                yield node.items
            else:
                yield node

    def build_tree(self, arr):
	"""Creates a trie from the array given using title as the key.
	"""
        for book in arr:
            self.add(book.title, book)

    def build_authors(self, arr):
	"""Creates a trie from the array given using the author of
	each book as a key. The value stored is a list of all the books
	written by that author.
	"""

        s = []  #a list of surname-book tuples
        for b in arr:
            for a in b.authors:
                s.append((a.lastname, b))
        d = defaultdict(list)

        for k, v in s:
            d[k].append(v)

        for surname, value in d.items():
            self.add(surname, value)



