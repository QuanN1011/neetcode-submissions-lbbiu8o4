class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def swap(i, j):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
        
        i, left, right = 0, 0, len(nums) - 1

        while i <= right:
            if nums[i] == 0:
                swap(i, left)
                left += 1
                i += 1
            elif nums[i] == 2:
                swap(i, right)
                right -= 1
            else:
                i += 1