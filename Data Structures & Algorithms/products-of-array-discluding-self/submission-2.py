class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1] * n
        suffix = [1] * n
        output = [0] * n

        for i in range(1, n):
            prefix[i] = nums[i - 1] * prefix[i-1]
            suffix[n - i - 1] = nums[n - i] * suffix[n - i]

        for i in range(n):
            output[i] = prefix[i] * suffix[i]

        return output