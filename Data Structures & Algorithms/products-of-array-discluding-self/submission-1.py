class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        numOfZeros = 0
        for num in nums:
            if (num == 0):
                numOfZeros += 1
                continue
            product *= num
        
        res = [0]*len(nums)

        if (numOfZeros >= 2):
            pass
        elif (numOfZeros == 1):
            for i in range(len(res)):
                if nums[i] == 0:
                    res[i] = product
                else:
                    res[i] = 0
        else:                    
            for i in range(len(res)):
                pass                
                res[i] = int(product/nums[i])
        return res
