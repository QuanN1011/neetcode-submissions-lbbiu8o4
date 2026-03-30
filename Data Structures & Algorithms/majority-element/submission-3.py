class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        major = math.floor(len(nums)/2)
        count = {}
        for i in nums:
            count[i] = count.get(i, 0) + 1; # can use defaultdict(int) to do += 1

        for i in nums:
            if(count[i] > major):
                return i
        return 0

        