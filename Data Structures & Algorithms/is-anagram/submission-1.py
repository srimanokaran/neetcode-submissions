class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letterMap = {}
        if len(s) != len(t): 
            return False
        for chars in s:
            letterMap[chars] = letterMap.get(chars, 0) + 1
        for chars in t:
            if (letterMap.get(chars, 0) == 0):
                return False
            letterMap[chars] = letterMap.get(chars, 0) - 1
        return True
            