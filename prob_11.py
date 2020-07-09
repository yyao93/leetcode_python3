class Solution:
    def maxArea(self, height: List[int]) -> int:
        if len(height) <= 1:
            return 0
        p1, p2 = 0, len(height) - 1
        ret = 0
        while p1 < p2:
            ret = max(ret, min(height[p1], height[p2]) * (p2 - p1))
            if height[p1] < height[p2]:
                p1 += 1
            else:
                p2 -= 1
        return ret
