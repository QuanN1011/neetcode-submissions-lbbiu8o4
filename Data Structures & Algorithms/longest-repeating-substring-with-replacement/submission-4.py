class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l, res = 0, 0

        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            windowSize = r - l + 1
            diff = windowSize - max(count.values())

            if diff <= k:
                res = windowSize
            else:
                count[s[l]] -= 1
                l += 1

        return res

