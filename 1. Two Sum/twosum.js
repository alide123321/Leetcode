/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function (nums, target) {
  let map = nums.map((val, indx) => [val, indx]);
  map.sort((a, b) => a[0] - b[0]);

  let lp = 0;
  let rp = map.length - 1;

  while (lp < rp) {
    if (map[lp][0] + map[rp][0] == target) return [map[lp][1], map[rp][1]];
    if (map[lp][0] + map[rp][0] < target) lp += 1;
    else rp -= 1;
  }
};
