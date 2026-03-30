class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        left , right = len(word1), len(word2)
        res = []
        l, r = 0, 0
        while l < left or r < right:
            if l < left:
                res.append(word1[l])
            if r < right:
                res.append(word2[r])
            l += 1
            r += 1
        
        return "".join(res)