class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(ch for ch in s if (ch.isalnum())).lower()

        # store str as a char count
        ch_count = [0]*len(s)
        reverse_txt = s[::-1]
        for idx, value in enumerate(s):
            ch_count[idx] = ord(value)
        for idx, value in enumerate(reverse_txt):
            ch_count[idx] -= ord(value)
            if ch_count[idx] != 0:
                return False
        return True

        

            
