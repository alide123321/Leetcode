class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hash = {nums[i] :i for i in range(len(nums))}
        
        for i in range(len(nums)):
            if ((target - nums[i]) in nums):
                if hash[target - nums[i]] == i: continue
                
                return [i, hash[target - nums[i]]]

        return None

