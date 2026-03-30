class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)
        output = [0] * len(nums)
        n = len(nums) - 1

        for i in range(1, len(nums)):
                prefix[i] = nums[i - 1] * prefix[i - 1]
                suffix[n - i] = nums[len(nums) - i] * suffix[len(nums) - i]

        for i in range(len(nums)):
            output[i] = prefix[i] * suffix[i]

        return output