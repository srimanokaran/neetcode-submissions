class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        map_of_sorted_strings = {}

        for string in strs:
            sorted_str = "".join(sorted(string))
            if sorted_str in map_of_sorted_strings:
                map_of_sorted_strings[sorted_str].append(string)
            else:
                map_of_sorted_strings[sorted_str] = [string]
        
        for value in map_of_sorted_strings.values():
            res.append(value)

        return res
        