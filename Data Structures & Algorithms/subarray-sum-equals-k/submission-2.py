class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum = {0: 1}
        res, sum = 0, 0

        for num in nums:
            sum += num
            if (sum - k) in prefixSum:
                res += prefixSum[sum-k]
            prefixSum[sum] = prefixSum.get(sum, 0) + 1
        return res