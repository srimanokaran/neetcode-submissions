class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letterMap = {}
        if len(s) != len(t): 
            return False
        for chars in s:
            letterMap[chars] = letterMap.get(chars, 0) + 1
        for chars in t:
            if (chars not in letterMap):
                return False
            letterMap[chars] = letterMap.get(chars, 0) - 1
        for value in letterMap.values():
            if (value != 0):
                return False
        return True
            