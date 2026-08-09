class Solution:
    
    def foreignDictionary(self, words: List[str]) -> str:
        self.time = 1
        graph = {}

        n = len(words)
        for i in range(n):
            w1 = words[i]
            for c in w1:
                if c not in graph:
                    graph[c] = {
                        "nei": set(),
                        "start": None,
                        "end": None
                    }
            for j in range(i+1,n):
                w2 = words[j]
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

        from pprint import pprint
        pprint(graph)
        return "".join([x[1] for x in ans])









