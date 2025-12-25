/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function (x) {
  let sX = x.toString();
  let i = 0,
    j = sX.length - 1;

  while (i < j) if (sX[i++] != sX[j--]) return false;

  return true;
};
