class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = {}
        ord_a = ord('a')

        for word in strs:
            counts = [0] * 26
            for ch in word:
                counts[ord(ch) - ord_a] += 1

            tuple_counts = tuple(counts)
            if tuple_counts in m:
                m[tuple_counts].append(word)
            else:
                m[tuple_counts] = [word]
    
        return list(m.values())
        