class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        threshold = len(nums) // 2

        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        for number, freq in count.items():
            if freq > threshold:
                return number