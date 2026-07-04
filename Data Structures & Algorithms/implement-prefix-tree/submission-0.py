class PrefixTree:

    def __init__(self):
        self.trie = {}

    def insert(self, word: str) -> None:
        m = self.trie
        def helper(c, m):
            if c not in m:
                m[c] = {
                    'ends': False
                }
            m = m[c]
            return m
        for c in word:
            m = helper(c, m)
        m["ends"] = True

    def search(self, word: str) -> bool:
        m = self.trie
        for c in word:
            if c not in m:
                return False
            m = m[c]
        return m["ends"]

    def startsWith(self, prefix: str) -> bool:
        m = self.trie
        for c in prefix:
            if c not in m:
                return False
            m = m[c]
        return True



        