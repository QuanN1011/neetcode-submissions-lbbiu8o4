class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = [0] * len(height)
        maxRight = [0] * len(height)
        minHeight = [0] * len(height)

        for i in range(1, len(height)):
            maxLeft[i] = max(maxLeft[i-1], height[i-1])
            maxL = maxLeft[i]

        for i in range(len(height) - 2, -1, - 1):
            maxRight[i] = max(maxRight[i+1], height[i+1])
            maxR = maxRight[i]

        for i in range(len(height)):
            minHeight[i] = min(maxLeft[i], maxRight[i])
        
        output = 0
        for i in range(len(height)):
            cur = minHeight[i] - height[i]
            output += max(0, cur)
        return output