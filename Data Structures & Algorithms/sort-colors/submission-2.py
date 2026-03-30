class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # buckets for bucket count
        count = [0, 0, 0]

        # count for each bucket
        for num in nums:
            count[num] += 1

        # modify nums
        index  = 0
        for i in range(3):
            while count[i]:
                count[i] -= 1
                nums[index] = i
                index += 1