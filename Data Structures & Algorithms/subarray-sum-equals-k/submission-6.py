class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = {0:1}
        res, cur = 0, 0
        for num in nums:
            cur += num
            if (cur - k) in prefix:
                res += prefix[cur - k]
            prefix[cur] = prefix.get(cur, 0) + 1

        return res