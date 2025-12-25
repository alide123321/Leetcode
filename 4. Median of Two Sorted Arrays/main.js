/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var findMedianSortedArrays = function (nums1, nums2) {
  let merged = [];
  let i = 0,
    j = 0,
    m = nums1.length,
    n = nums2.length;
  let length = m + n;
  while (i < m && j < n) {
    if (nums1[i] < nums2[j]) merged.push(nums1[i++]);
    else merged.push(nums2[j++]);
  }

  while (i < m) merged.push(nums1[i++]);
  while (j < n) merged.push(nums2[j++]);

  if (length % 2 == 1) return merged[Math.floor(length / 2)];

  let Mid = length / 2;
  return (merged[Mid - 1] + merged[Mid]) / 2;
};
