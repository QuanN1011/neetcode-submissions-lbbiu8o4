class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l, left, r, right = 0, len(word1), 0, len(word2)
        res = []
        while l < left or r < right:
            if l < left:
                res.append(word1[l])
            if r < right:
                res.append(word2[r])
            l, r = l + 1, r + 1
        
        return "".join(res)