class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        countS1, countS2 = {}, {}

        for c in s1:
            countS1[c] = countS1.get(c, 0) + 1
        
        L = 0
        windowSize = len(s1)
        for R in range(len(s2)):
            countS2[s2[R]] = countS2.get(s2[R], 0) + 1
            curWindow = R - L + 1

            if curWindow > windowSize:
                countS2[s2[L]] -= 1
                if countS2[s2[L]] == 0:
                    del countS2[s2[L]]
                L += 1
            
            if countS1 == countS2:
                return True
        
        return False