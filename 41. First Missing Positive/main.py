class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        hashSet = set(nums[i] for i in range(len(nums)))
        lowest = 1

        while lowest in hashSet:
            lowest += 1

        return lowest