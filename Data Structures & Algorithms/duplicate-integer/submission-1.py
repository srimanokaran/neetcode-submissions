class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique = set()

        for num in nums:
            if (num in unique):
                return True
            unique.add(num)
        return False
        # 1. put the values in a set

        