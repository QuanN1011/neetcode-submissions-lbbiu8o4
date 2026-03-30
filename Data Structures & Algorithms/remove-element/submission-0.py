class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        length = len(nums)
        count = 0
        i = 0
        while i < n:
            if nums[i] == val:
                nums.remove(nums[i])
                n -= 1
                count += 1
            else:
                i += 1


        return length - count

