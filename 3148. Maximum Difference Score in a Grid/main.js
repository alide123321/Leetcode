/**
 * @param {number[][]} grid
 * @return {number}
 */
var maxScore = function (grid) {
  const ROWS = grid.length;
  const COLUMNS = grid[0].length;
  const MIN = -100000000;
  let max = MIN;
  maxDiff(0, 0);
  return max;

  function maxDiff(row, col) {
    if (row >= ROWS - 1 || col >= COLUMNS - 1)
      return grid[Math.min(row, ROWS - 1)][Math.min(col, COLUMNS - 1)];

    let right = maxDiff(row, col + 1);
    let bottom = maxDiff(row + 1, col);
    let relativeMax = Math.max(right, bottom);
    relativeMax -= grid[row][col];
    max = Math.max(relativeMax, max);
    return max;
  }
};

let input = [
  [9, 5, 7, 3],
  [8, 9, 6, 1],
  [6, 7, 14, 3],
  [2, 5, 3, 1],
];
console.log(maxScore(input)); //output: 9
