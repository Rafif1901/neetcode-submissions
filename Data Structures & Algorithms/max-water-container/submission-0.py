class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #area = (h[r]-h[l]) * min(l, r)
        n = len(heights)-1
        l = max_area =0
        r = n
        while l<r:
            area = (r-l) * min(heights[l], heights[r])
            max_area = max(area, max_area)
            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1
        return max_area