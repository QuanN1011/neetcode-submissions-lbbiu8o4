class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # initialize prefix and suffix, output array
        # left to right pass
            #
        # right to left pass

        output = [0] * len(nums)
        prefix = 1

        for i in range(len(nums)):
            output[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for j in range(len(nums) - 1, -1, -1):
            output[j] *= suffix
            suffix *= nums[j]

        return output