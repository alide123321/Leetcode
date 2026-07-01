import java.util.HashMap;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> seenMap = new HashMap<Integer, Integer>();

        for (int i = 0; i < nums.length; ++i) {
            int needed = target - nums[i];
            if (seenMap.containsKey(needed)) {
                return new int[] { seenMap.get(needed), i };
            }

            seenMap.put(nums[i], i);
        }

        return new int[2];
    }
}