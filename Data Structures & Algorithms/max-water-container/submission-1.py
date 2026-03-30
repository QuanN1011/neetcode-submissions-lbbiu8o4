class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        maxContainer = 0
        while l < r:
            width = r - l
            height = min(heights[l], heights[r])
            maxContainer = max(maxContainer, width * height)

            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return maxContainer