/**
 * @param {string} s
 * @param {string} p
 * @return {boolean}
 */
var isMatch = function (s, p) {
  let regex = "";
  for (let i = 0; i < p.length; i++) {
    if (i + 1 < p.length && p[i + 1] === "*") {
      regex += p[i] === "." ? ".*" : `(${p[i]})*`;
      i++;
    } else {
      regex += p[i];
    }
  }
  return new RegExp("^" + regex + "$").test(s);
};
