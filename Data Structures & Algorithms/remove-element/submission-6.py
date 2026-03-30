class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # push elements to be removed towards the end of list
        # set k = 0
        # loop through list
            # check if current value is equal to val
            # if not, set nums at pointer k equal to num's at i
            # increment k


        i = 0
        n = len(nums)
        while i < n:
            if nums[i] == val:
                n -= 1
                nums[i] = nums[n]
            else:
                i += 1
            
        return n



