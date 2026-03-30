class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # push elements to be removed towards the end of list
        # set k = 0
        # loop through list
            # check if current value is equal to val
            # if not, set nums at pointer k equal to num's at i
            # increment k


        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1  

        return k



