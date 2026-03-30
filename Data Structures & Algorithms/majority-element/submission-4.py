class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        major = math.floor(len(nums)/2)
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1

        for num in nums:
            if count[num] > major:
                return num

    

        