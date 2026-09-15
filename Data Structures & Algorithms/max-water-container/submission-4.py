class Solution:
    def maxArea(self, heights: List[int]) -> int:

        l, r = 0, len(heights) - 1
        maxArea = 0

        while l < r:

            h1 = heights[l]
            h2 = heights[r]

            area = min(h1, h2) * (r - l)

            maxArea = area if area > maxArea else maxArea

            if h1 < h2:
                l += 1
            elif h2 < h1:
                r -= 1
            else:
                l +=1
                r -= 1
        
        return maxArea



        