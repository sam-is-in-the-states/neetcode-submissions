class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        results = defaultdict(list)

        def get_string_hash(s):
            a = [0]*26
            for c in s:
                a[ord(c) - ord('a')] += 1
            return ",".join(str(ch) for ch in a)
        for s in strs:
            hash_s = get_string_hash(s)
            results[hash_s].append(s)
        
        if not results:
            return []
        print(results)
        return [
            v for k, v in results.items()
        ]
            