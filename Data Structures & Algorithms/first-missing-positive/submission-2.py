class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        numSet = set(nums)
        missing = 1

        for num in nums:
            if num > 0 and missing == num:
                missing += 1
                length = 1
                while num + length in numSet:
                    missing += 1
                    length += 1
        return missing

        