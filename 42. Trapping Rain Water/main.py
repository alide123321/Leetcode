class Solution:
    def trap(self, height: List[int]) -> int:
        
        LP , RP = 0,  len(height) - 1
        maxL, maxR = height[LP], height[RP]
        output = 0

        while LP <= RP:

            waterAmount = 0

            if maxL <= maxR:

                waterAmount = maxL - height[LP]
                maxL = max(maxL, height[LP])
                LP += 1
            else:

                waterAmount = maxR - height[RP]
                maxR = max(maxR, height[RP])
                RP -= 1

            if waterAmount > 0:
                output += waterAmount


        return output