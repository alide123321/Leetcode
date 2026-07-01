/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function (s) {
  if (s.length <= 1) return s.length;

  let lp = 0;
  let maxCount = 1;
  let letters = new Map();

  for (let rp = 0; rp < s.length; ++rp) {
    if (letters.has(s[rp]) && letters.get(s[rp]) >= lp) {
      lp = letters.get(s[rp]) + 1;
    }

    letters.set(s[rp], rp);
    maxCount = Math.max(maxCount, rp - lp + 1);
  }

  return maxCount;
};
