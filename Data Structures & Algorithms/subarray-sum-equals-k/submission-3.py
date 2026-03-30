class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum = {0: 1}
        res, currentSum = 0, 0

        for num in nums:
            currentSum += num
            if (currentSum - k) in prefixSum:
                res += prefixSum[currentSum-k]
            prefixSum[currentSum] = prefixSum.get(currentSum, 0) + 1
        return res