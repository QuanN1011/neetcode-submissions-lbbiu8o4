class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        L , res = 0, 0

        for R in range(len(s)):
            count[s[R]] = count.get(s[R], 0) + 1
            windowSize = R - L + 1
            diff = windowSize - max(count.values())

            if diff <= k:
                res = windowSize
            else:
                count[s[L]] -= 1
                L += 1
        return res