class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = [0] * len(height)
        for i in range(1, len(height)):
            maxLeft[i] = max(maxLeft[i-1], height[i-1])

        maxRight = [0] * len(height)
        for i in range(len(height) - 2, -1, -1):
            maxRight[i] = max(maxRight[i+1], height[i+1])

        minArr = [0] * len(height)
        for i in range(len(height)):
            minArr[i] = min(maxLeft[i], maxRight[i])

        output = 0
        for i in range(len(height)):
            cur = minArr[i] - height[i]
            output += max(0, cur)

        return output