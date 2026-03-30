class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            target = -1 * nums[i]
            j = i + 1
            k = len(nums) - 1
            # skip duplicate for i
            if i > 0 and nums[i] == nums[i-1]:
                continue

            while j < k:
                curSum = nums[j] + nums[k]
                if curSum == target:
                    res.append([nums[i], nums[j], nums[k]])
                    j, k = j + 1, k - 1
                    # skip dupls for j and k
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                    while k > j and nums[k] == nums[k+1]:
                        k -= 1
                elif curSum > target:
                    k -= 1
                else:
                    j += 1
            
        return res