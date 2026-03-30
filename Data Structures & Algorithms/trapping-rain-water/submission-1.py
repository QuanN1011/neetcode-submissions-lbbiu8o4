class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxLeft, maxRight = height[l], height[r]
        output = 0

        while l < r:
            if maxLeft <= maxRight:
                l += 1
                cur = maxLeft - height[l]
                output += max(0, cur)
                maxLeft = max(maxLeft, height[l])
            else:
                r -= 1
                cur = maxRight - height[r]
                output += max(0, cur)
                maxRight = max(maxRight, height[r])
        return output
