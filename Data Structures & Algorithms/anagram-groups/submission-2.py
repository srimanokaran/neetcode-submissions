class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_map = {}
        

        # sorting is the bottle neck
        for word in strs:
            count = [0]*26
            for ch in word:
                count[ord(ch) - ord('a') ] += 1
            tuple_count = tuple(count)
            if (tuple_count not in str_map):
                str_map[tuple_count] = [word]
            else:
                str_map[tuple_count].append(word)
        
        return list(str_map.values())


