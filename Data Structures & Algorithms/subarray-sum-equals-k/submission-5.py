class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = {0:1}
        res, curSum = 0,0
        for i in range(len(nums)):
            curSum += nums[i]
            diff = curSum - k
            if diff in prefix:
                res += prefix[diff]
            prefix[curSum] = prefix.get(curSum, 0) + 1

        return res
