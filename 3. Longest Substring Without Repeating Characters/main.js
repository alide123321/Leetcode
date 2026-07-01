/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function (s) {
  if (s.length <= 1) return s.length;

  let lp = 0;
  let maxCount = 1;
  let letters = new Set();

  for (let rp = 0; rp < s.length; ++rp) {
    while (letters.has(s[rp])) {
      letters.delete(s[lp]);
      ++lp;
    }

    letters.add(s[rp]);
    maxCount = Math.max(maxCount, rp - lp + 1);
  }

  return maxCount;
};
