class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        countS1 = {}
        countS2 = {}

        for char1 in s1:
            countS1[char1] = countS1.get(char1, 0) + 1

        L = 0
        k = len(s1)

        for R in range(len(s2)):
            countS2[s2[R]] = countS2.get(s2[R], 0) + 1
            windowSize = R - L + 1
            
            if windowSize > k:
                countS2[s2[L]] -= 1
                if countS2[s2[L]] == 0:
                    del countS2[s2[L]]
                L += 1
                
            if countS2 == countS1:
                return True
        
        return False
                