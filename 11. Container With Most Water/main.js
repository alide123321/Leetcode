/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function (height) {
  let n = height.length;
  let i = 0,
    j = n - 1;
  let maxVolume = 0;

  while (i < j) {
    let volume = (j - i) * (height[i] < height[j] ? height[i] : height[j]);
    if (volume > maxVolume) maxVolume = volume;
    height[i] < height[j] ? ++i : --j;
  }
  return maxVolume;
};
