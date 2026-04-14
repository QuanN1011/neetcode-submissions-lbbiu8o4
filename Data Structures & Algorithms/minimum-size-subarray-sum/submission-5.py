class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        curSum, output = 0, float('inf')
        l = 0

        for r in range(len(nums)):
            curSum += nums[r]

            while curSum >= target:
                output = min(output, r - l + 1)
                curSum -= nums[l]
                l += 1
            
        return output if output != float('inf') else 0