class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        left, right = len(word1), len(word2)
        l, r = 0, 0

        while l < left and r < right:
            res += word1[l] + word2[r]
            l, r = l + 1, r + 1
        
        while l < left:
            res += word1[l]
            l += 1
        
        while r < right:
            res += word2[r]
            r += 1

        return res