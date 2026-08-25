class Solution:
    def isValid(self, s: str) -> bool:
        open_stack = []
        char_map = {')': '(', ']': '[', '}': '{'}
        for ch in s:
            if ch not in char_map:
                # Open char
                open_stack.append(ch)
            else:
                # Theres a closed char but no open char
                if (len(open_stack) == 0):
                    return False
                open_char = open_stack.pop()
                if (char_map[ch] != open_char):
                    return False
        
        return len(open_stack) == 0
