class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum = {0:1} # base case
        res, currentSum = 0, 0

        for num in nums:
            currentSum += num
            diff = currentSum - k
            if diff in prefixSum:
                res += prefixSum[diff]
            prefixSum[currentSum] = prefixSum.get(currentSum, 0) + 1

        return res