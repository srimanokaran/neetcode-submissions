class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxDiff = 0
        for i in range(0, len(prices)):
            diff = -1
            for j in range(i + 1, len(prices)):
                diff = prices[j] - prices[i]
                if (diff > maxDiff):
                    maxDiff = diff
        return maxDiff
            