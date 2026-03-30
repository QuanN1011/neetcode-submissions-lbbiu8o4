class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, left, right = 0, 0, len(nums) - 1
        def swap(i, j):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
        while i <= right:
            if nums[i] == 0:    # if == 1, swap with left pointer
                swap(i, left)
                left += 1
                i += 1 
            elif nums[i] == 2: # swap with right pointer
                swap(i, right)
                right -= 1  # don't increment i in case 0 got moved to the middle
            else:    # == 1, just increment i
                i += 1