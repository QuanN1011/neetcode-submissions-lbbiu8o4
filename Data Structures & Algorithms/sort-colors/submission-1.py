class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # one pass with two pointers, one with each end ignoring 1s
        i, left, right = 0, 0, len(nums) - 1

        # swap function
        def swap(i, j):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp

        # while loop to iterate through   
        while i <= right:
            if nums[i] == 0:
                swap(i, left)
                i += 1
                left += 1
            elif nums[i] == 2:
                swap(i, right)
                right -= 1
            else:
                i += 1