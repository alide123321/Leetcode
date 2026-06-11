/**
 * @param {number} n
 * @return {number}
 */
var climbStairs = function (n) {
  let mem = [];

  return rec(n);

  function rec(n) {
    if (mem[n] != undefined) return mem[n];
    if (n == 0) return 1;
    if (n < 0) return 0;

    mem[n] = rec(n - 1) + rec(n - 2);

    return mem[n];
  }
};

console.log(climbStairs(4));
