class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxL, maxR = height[l], height[r]
        output = 0
        
        while l < r:
            if maxL < maxR:
                l += 1
                output += max(0, maxL - height[l])
                maxL = max(maxL, height[l])
            else:
                r -= 1
                output += max(0, maxR - height[r])
                maxR = max(maxR, height[r])
        
        return output