class Solution:
    
    def foreignDictionary(self, words: List[str]) -> str:
        self.time = 1
        graph = {}
        n = len(words)

        for word in words:
            for c in word:
                if c not in graph:
                    graph[c] = {
                        "nei": set(),
                        "start": None,
                        "end": None
                    }
        for i in range(n-1):
            w1 = words[i]
            j = i+1
            w2 = words[j]
            if w1 == w2:
                continue
            i1,i2 = 0,0
            while i1 < len(w1) and i2 < len(w2) and w1[i1] == w2[i2]:
                i1 += 1
                i2 += 1
            
            if i1 != len(w1) and i2 == len(w2):
                return ""

            if i1 == len(w1):
                continue

            graph[w1[i1]]["nei"].add(w2[i2])

        def dfs(c):
            g = graph[c]

            if g["start"] and not g["end"]:
                raise ValueError("Cycle")
            if g["start"] and g["end"]:
                return

            g["start"] = self.time
            self.time += 1
            for n in g["nei"]:
                dfs(n)
            g["end"] = self.time
            self.time += 1

        for k, v in graph.items():
            if v["start"]:
                continue
            try:
                dfs(k)
            except ValueError:
                return ""
        
        ans = []
        for k, v in graph.items():
            ans.append((v["end"], k))
        ans.sort(key=lambda x: x[0], reverse=True)

        return "".join([x[1] for x in ans])









