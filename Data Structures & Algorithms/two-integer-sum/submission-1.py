class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        difference_map = dict()

        for index, num in enumerate(nums):
            if num in difference_map:
                return [difference_map[num], index]

            difference = target - num
            difference_map[difference] =  index
        return [0,0]