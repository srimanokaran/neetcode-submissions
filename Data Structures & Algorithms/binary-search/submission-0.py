class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Get middle of the array,
        # if target == middle, return index
        # Is target > middle?
        # if yes, find middle of middle + 1 to the end of the array
        # else, find middle of 0 -> middle, then repeat process
        
        l, r = 0, len(nums) - 1
        
        while (l <= r):
            mid = (l + r) // 2
            if (target == nums[mid]):
                return mid
            if target > nums[mid]:
                l = mid + 1
                continue
            elif target < nums[mid]:
                r = mid - 1
                continue
        return -1