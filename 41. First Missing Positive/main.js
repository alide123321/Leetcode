/**
 * @param {number[]} nums
 * @return {number}
 */
var firstMissingPositive = function (nums) {
  let numMap = new Map();
  let lowest = 1;
  for (let i = 0; i < nums.length; i++) {
    if (nums[i] <= 0) continue;
    numMap.set(nums[i], true);
  }

  while (numMap.has(lowest)) {
    ++lowest;
  }

  return lowest;
};
