class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # store frequency in a hash map
        # key = num, value = frequency
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1

        # use bucket sort
        buckets = [[] for i in range(len(nums) + 1)]

        # nums = [7, 7], k = 1 
        # [[], [], [7]], index corresponds to the count, so the length of bucket is always 
        # equal to the size of the arr

        # Loop through bucket, check if there is anything with that count, if not, move on
        # if yes, then put the num in that bucket and move on

        for num, freq in count.items():
            buckets[freq].append(num)
        
        res = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                res.append(num)
            if (len(res) == k):
                return res
        return res
        

