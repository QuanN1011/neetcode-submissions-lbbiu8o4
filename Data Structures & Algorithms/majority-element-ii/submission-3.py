class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        major = len(nums) // 3
        count = {}
        for num in nums:
            count[num] = count.get(num,0) + 1
        
        res = []
        for num, f in count.items():
            if f > major:
                res.append(num)
        return res