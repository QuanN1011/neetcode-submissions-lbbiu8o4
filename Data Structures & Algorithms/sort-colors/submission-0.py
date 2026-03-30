class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # bucket sort
        bucketZero, bucketOne, bucketTwo = 0, 0, 0

        # count the nums in bucket
        for num in nums:
            if num == 0:
                bucketZero += 1
            elif num == 1:
                bucketOne += 1
            else:
                bucketTwo += 1
        
        # fill 0
        for i in range(bucketZero):
            nums[i] = 0
        # fill 1
        for j in range(bucketZero, bucketZero + bucketOne):
            nums[j] = 1
        # fill 2
        for k in range(bucketZero + bucketOne, bucketZero + bucketOne + bucketTwo):
            nums[k] = 2

