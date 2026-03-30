class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # set major rate
        # have a hashmap to count
        # loop through list
        # add element to map
        # check if freq of elemnt is greater than major rate

        major = math.floor(len(nums)/2)
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1

        for c in count:
            if count[c] > major:
                return c

        