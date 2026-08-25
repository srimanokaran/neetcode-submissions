import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #key = number
        #value = frequency of the number
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        heap = []
        for num, frequency in count.items():
            heapq.heappush(heap, (-frequency, num))
        
        res = []
        for _ in range(k):
            frequency, num = heapq.heappop(heap)
            res.append(num)
        return res
        
        

        

