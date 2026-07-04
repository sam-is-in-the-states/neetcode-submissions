class WordDictionary:

    def __init__(self):
        self.trie = {
            "ends": False
        }

    def addWord(self, word: str) -> None:
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
        def helper(m, word, idx):
            if idx == len(word):
                return m["ends"]
            
            c = word[idx]
            if c in m:
                return helper(m[c], word, idx+1)
            
            if c == '.':
                for l in m:
                    if l == "ends":
                        continue
                    if helper(m[l], word, idx+1):
                        return True
            
            return False
        return helper(self.trie, word, 0)

