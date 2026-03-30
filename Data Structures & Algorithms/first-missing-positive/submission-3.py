class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # loop through negatives to change to 0, dont care negatives
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0
        
        # if value - 1, change arr val at (value - 1) to be negative
        for i in range(len(nums)):
            val = abs(nums[i])
            if 1 <= val <= len(nums):
                if nums[val - 1] > 0:
                    nums[val-1] *= -1
                elif nums[val-1] == 0:
                    nums[val - 1] = -1 * (len(nums) + 1)

        # check if values are negative or 0 then return, else return len + 1
        for i in range(1, len(nums) + 1):
            if nums[i - 1] >= 0:
                return i
        return len(nums) + 1

        