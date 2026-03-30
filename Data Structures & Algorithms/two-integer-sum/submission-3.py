class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum = {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in sum:
                return [sum[diff], i]
            sum[num] = i
            
        return [0,0]
