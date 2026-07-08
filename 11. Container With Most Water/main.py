class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        output, lp, rp,  = 0, 0, len(height) - 1

        while lp < rp:
            left, right = height[lp], height[rp]
            output = max(output, (rp-lp) * min(left, right))

            if left <= right:
                lp += 1
            else:
                rp -= 1

        return output