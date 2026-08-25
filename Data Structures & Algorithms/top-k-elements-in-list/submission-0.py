class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Store elements in a dict with [K: Num V: Freq], pick the first k from V from dict
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        res = []
        while k > 0:
            num = max(freq, key = freq.get)
            k -= 1
            del freq[num]
            res.append(num)
        return res
            
